from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession

from database.db_helper import async_session
from fa_project import User
from posts.views import get_all_posts
from src.fa_project.auth.auth import get_jwt_strategy
from users.dependencises import current_active_user

get_jwt_strategy = get_jwt_strategy()

router = APIRouter(
    tags=["Pages"],
)

templates = Jinja2Templates(directory="src/fa_project/templates")


@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse(name="base.html", context={"request": request})


@router.get("/main")
async def get_main_page(request: Request, session: AsyncSession = Depends(async_session)):
    try:
        if request.cookies["FastAPI-Auth"]:
            all_posts = await get_all_posts(session)
            return templates.TemplateResponse(name="main_page.html", context={"request": request, "data": all_posts})
    except KeyError:
        return templates.TemplateResponse(name="auth.html", context={"request": request})


@router.get("/profile/{uuid}")
def get_user_page(request: Request, user: User = Depends(current_active_user)):
    try:
        if request.cookies["FastAPI-Auth"]:
            return templates.TemplateResponse(name="user_page.html", context={"request": request, "data": user})
    except KeyError:
        print("No cookie")
        return templates.TemplateResponse(name="auth.html", context={"request": request})
