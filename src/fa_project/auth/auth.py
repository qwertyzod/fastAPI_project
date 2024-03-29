
from fastapi_users.authentication import CookieTransport, AuthenticationBackend, JWTStrategy
import uuid

from fastapi_users import FastAPIUsers

from src.fa_project.users.manager import get_user_manager
from src.fa_project.models import User

from src.fa_project.settings import settings

cookie_transport = CookieTransport(
    cookie_name="FastAPI-Auth",
    cookie_max_age=3600,
)


def get_jwt_strategy() -> JWTStrategy:
    """Возвращает стратегию для аутентификации с помощью JWT"""
    return JWTStrategy(secret=settings.SECRET, lifetime_seconds=1800)


auth_backend = AuthenticationBackend(
    name="FastAPI-Auth",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])
