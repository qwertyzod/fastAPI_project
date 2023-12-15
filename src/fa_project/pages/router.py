from fastapi import APIRouter, Request, Response, Depends, Cookie, Response
from fastapi.templating import Jinja2Templates
from fastapi_users.jwt import decode_jwt

from src.fa_project.auth.auth import get_jwt_strategy


get_jwt_strategy = get_jwt_strategy()

router = APIRouter(
    tags=["Pages"],
)

templates = Jinja2Templates(directory="src/fa_project/templates")


@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse(name="base.html", context={"request": request})

@router.get("/main")
async def get_main_page(request: Request, response: Response):
    try:
        if request.cookies["FastAPI-Auth"]:
            return templates.TemplateResponse(name="main_page.html", context={"request": request})
    except KeyError:
        return templates.TemplateResponse(name="auth.html", context={"request": request})

@router.get("/profile/{uuid}")
def get_user_page(request: Request):
    try:
        if request.cookies["FastAPI-Auth"]:
            return templates.TemplateResponse(name="user_page.html", context={"request": request})
    except KeyError:
        return templates.TemplateResponse(name="auth.html", context={"request": request})