from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    DB_connection: str
    SUPABASE_URL: str
    SUPABASE_KEY: str

setting = Settings()