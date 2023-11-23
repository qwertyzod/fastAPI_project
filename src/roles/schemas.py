from pydantic import BaseModel

class RoleBaseSchema(BaseModel):
    """Базовая схема пользователя"""
    id: int
    name: str
    permissions: str

