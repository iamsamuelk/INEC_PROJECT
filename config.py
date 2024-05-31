from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "https://http://127.0.0.1:8000/"
    SQLALCHEMY_DATABASE_URL: str = (
        "postgresql://vgsykulb:xsMjB35xK8R5wiNakTbmdl0pB8PY5tQk@"
        "drona.db.elephantsql.com/vgsykulb"
    )


class Config:
    env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
