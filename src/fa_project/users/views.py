from fastapi import APIRouter, Depends

from src.fa_project.models import User
from users.dependencises import current_active_user
from users.schemas import UserRead

router = APIRouter(tags=['Пользователи'], prefix='/users')


@router.get('/user')
async def get_user(user: User = Depends(current_active_user)) -> UserRead:
    return user
