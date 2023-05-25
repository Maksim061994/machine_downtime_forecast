from pydantic import BaseSettings
import os

ENV_API = os.getenv("ENVIRONMENT")


class Settings(BaseSettings):
    # user
    secret_key: str
    algorithm: str
    access_token_expires_hours: int

    # clickhouse
    db_ch_host: str
    db_ch_port: int
    db_ch_protocol: str
    db_ch_user: str
    db_ch_password: str
    db_ch_database_models: str
    db_ch_table_models: str

    class Config:
        env_file = ".env" if not ENV_API else f".env.{ENV_API}"


def get_settings():
    return Settings()
