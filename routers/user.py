from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Header
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import JWTError, jwt, ExpiredSignatureError

from ..auth_utils import (get_current_user, authenticate_user, create_access_token, create_refresh_token)
from ..config import ALGORITHM, SECRET_KEY
from ..models.user import Token, User

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    refresh_token = create_refresh_token(data={"sub": user.username})

    return {"access_token": access_token, "token_type": "bearer", "refresh_token": refresh_token}


@router.post("/token/refresh")
async def refresh_access_token(refresh_token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    refresh_token_exception = HTTPException(
        status_code=401,
        detail="Expired refresh token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get('sub')
        if not username:
            raise credentials_exception
    except ExpiredSignatureError:
        raise refresh_token_exception
    except JWTError:
        raise credentials_exception

    new_access_token = create_access_token(data={"sub": username})
    return {"access_token": new_access_token, "token_type": "bearer"}


@router.get("/users/me", response_model=User)
async def read_current_user(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@router.get("/users/me/items/")
async def read_own_items(
        current_user: Annotated[User, Depends(get_current_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]
