from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "StatPage"
    debug: bool = False
    database_url: str = "sqlite:///./statpage.db"

    model_config = {"env_prefix": "STATPAGE_"}


settings = Settings()
