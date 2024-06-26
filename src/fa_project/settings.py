from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

env_file = f"{Path(__file__).parent.parent.parent}/.env"


class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int
    project_name: str = "FastAPI Project"
    SECRET: str
    DEBUG: bool
    SERVER_HOST: str
    SERVER_PORT: int

    model_config = SettingsConfigDict(env_file=env_file, env_file_encoding='utf-8', extra='ignore')

    @property
    def db_url(self) -> str:
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


settings = Settings()
