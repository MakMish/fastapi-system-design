from pydantic_settings import BaseSettings,SettingsConfigDict
class Setting(BaseSettings):
    model_config=SettingsConfigDict(env_file=".env",extra="ignore")
    db_url:str
    SECRET_KEY:str
    ALGORITHM:str
    ai_api:str
    cloud_name:str
    cloud_API_key:str
    cloud_api_secret:str
    gmail_app_password:str
    redis_url:str
    