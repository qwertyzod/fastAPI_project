from pydantic import BaseModel, EmailStr

class UserBaseSchema(BaseModel):
    """Базовая схема пользователя"""
    name: str
    email: EmailStr
    created_at: str

    class ConfigDict:
        """Конфигурация схемы"""
        from_attributes = True
