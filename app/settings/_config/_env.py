from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvSettingsFile(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", case_sensitive=True, extra="ignore"
    )
    BOT_TOKEN: str = ""
    GIT_TOKENS: list[str] = []
