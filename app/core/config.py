import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Palm Oil Model Classifier"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_ROOT_DIR: str = os.getenv("PROJECT_ROOT_DIR", os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    MODEL_PATH: str = os.path.join(PROJECT_ROOT_DIR, "data_tf")

    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore'
    )


settings = Settings()
