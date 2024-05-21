from fastapi import APIRouter, Depends

from src.fa_project.models import User
from users.dependencises import current_active_user

router = APIRouter(tags=['Пользователи'], prefix='/users')


@router.get('/user')
async def get_user(user: User = Depends(current_active_user)):
    return user
