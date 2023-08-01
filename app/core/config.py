from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):

    app_title: str = 'Кошачий благотворительный фонд'
    description: str = 'Сервис для поддержки котиков!'
    database_url: str = f'sqlite+aiosqlite:///./{app_title}fastapi.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    lifetime_seconds: int = 3600

    class Config:
        env_file = '.env'


settings = Settings()
