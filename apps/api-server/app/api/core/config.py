from pydantic_settings import (
    BaseSettings
)


class Settings(
    BaseSettings
):

    OPENAI_API_KEY: str
    REDIS_URL: str
    AUTH_URL: str


settings = Settings()