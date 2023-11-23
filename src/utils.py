import os
from pathlib import Path

from alembic.config import Config

from src.settings import settings


def get_alembic_config_from_db_url(db_url: str) -> Config:
    """Возвращает конфигурацию для Alembic"""
    db_url = db_url.replace('postgresql+asyncpg://', 'postgresql+psycopg2://')

    root_path = Path(__file__).parent.parent.parent
    alembic_config_path = root_path / 'alembic.ini'

    config = Config(alembic_config_path)
    alembic_location = config.get_main_option('script_location')

    if not os.path.isabs(alembic_location):
        config.set_main_option('script_location', str(root_path / alembic_location))

    if db_url is None:
        db_url = settings.db_url

    config.set_main_option('sqlalchemy.url', db_url)

    return config
