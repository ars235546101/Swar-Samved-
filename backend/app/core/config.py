from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Music Tutor API"
    SECRET_KEY: str = "change_me"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    DATABASE_URL: str = "postgresql+psycopg://postgres:postgres@db:5432/music_tutor"
    REDIS_URL: str = "redis://redis:6379/0"

    class Config:
        env_file = ".env"

settings = Settings()