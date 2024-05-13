from fastapi import FastAPI
from .routers.user import router as auth_router

app = FastAPI()

# Include the routers from routers.py
app.include_router(auth_router, tags=["Authentication"])
