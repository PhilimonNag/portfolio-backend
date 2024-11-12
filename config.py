from pydantic_settings import BaseSettings,SettingsConfigDict

class Configs(BaseSettings):
      model_config=SettingsConfigDict(env_file=".env")
      title:str
      desc:str
      mongo_url:str
      db_name:str
      port:int

config=Configs()