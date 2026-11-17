from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "PROJECT TITAN"
    environment: str = "development"
    api_v1_prefix: str = "/api/v1"
    database_url: str = "postgresql+psycopg://titan:titan@localhost:5432/titan"
    odds_api_key: str = ""
    odds_api_base_url: str = "https://api.the-odds-api.com"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
