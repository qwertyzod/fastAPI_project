from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

env_file = f"{Path(__file__).parent.parent}/.env"

class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int
    project_name: str = "FastAPI Project"

    model_config = SettingsConfigDict(env_file=env_file, env_file_encoding='utf-8')

    @property
    def db_url(self) -> str:
        """Возвращает URL для подключения к базе данных"""
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


settings = Settings()