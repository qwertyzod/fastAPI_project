import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from fastapi.middleware.cors import CORSMiddleware


from src.fa_project.auth.auth import auth_backend, fastapi_users
from settings import settings

from src.fa_project.users.schemas import UserRead, UserCreate
from src.fa_project.pages.router import router as router_pages
from src.fa_project.auth.router import router as router_auth
from src.fa_project.posts.views import router as router_posts




app = FastAPI(
    title="Test project FastAPI",
)

origins = [
    "http://localhost:3000",
]

app.mount('/static', StaticFiles(directory='src/fa_project/static'), name='static')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

app.include_router(router_pages)
app.include_router(router_auth)
app.include_router(router_posts)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=True
    )
