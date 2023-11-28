import uuid

import uvicorn
from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from starlette.middleware.cors import CORSMiddleware

from fa_project.auth.auth import auth_backend
from fa_project.settings import settings
from fa_project.users.manager import get_user_manager
from fa_project.users.models import User
from fa_project.users.schemas import UserRead, UserCreate

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

app = FastAPI(
    title="Test project FastAPI",
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        reload=True
    )
