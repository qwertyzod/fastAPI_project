from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi_users.jwt import decode_jwt
from jwt.exceptions import ExpiredSignatureError

from src.fa_project.auth.auth import get_jwt_strategy

router = APIRouter(
    tags=["auth"],
)

get_jwt_strategy = get_jwt_strategy()

templates = Jinja2Templates(directory="src/fa_project/templates")


@router.get("/registry")
def get_registry_page(request: Request):
    return templates.TemplateResponse(name="registry.html", context={"request": request})


@router.get("/auth")
def get_auth_page(request: Request):
    return templates.TemplateResponse(name="auth.html", context={"request": request})


@router.post("/token")
async def check_token(request: Request) -> str:
    try:
        if "FastAPI-Auth" in request.cookies:
            data = decode_jwt(
                request.cookies["FastAPI-Auth"],
                get_jwt_strategy.decode_key,
                get_jwt_strategy.token_audience,
                algorithms=[get_jwt_strategy.algorithm]
            )
            return data['sub']
    except ExpiredSignatureError:
        return 'Token expired'
