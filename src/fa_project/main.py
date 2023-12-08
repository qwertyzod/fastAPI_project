import uuid

import uvicorn
from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from auth.auth import auth_backend
from settings import settings
from users.manager import get_user_manager
from users.models import User
from users.schemas import UserRead, UserCreate

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

app = FastAPI(
    title="Test project FastAPI",
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=True
    )
