from pydantic import BaseModel
from typing import Optional


class Token(BaseModel):
    """
    Represents a token object.
    """
    access_token: str
    token_type: str
    refresh_token: Optional[str] = None


class TokenData(BaseModel):
    """
    Represents token data.
    """
    username: Optional[str] = None


class User(BaseModel):
    """
    Represents a user object.
    """
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDB(User):
    """
    Represents a user object stored in the database.
    """
    hashed_password: str
