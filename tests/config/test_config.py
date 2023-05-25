from pydantic import BaseSettings
from app.config.settings import Settings


class SettingsForTests(BaseSettings):
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
        env_file = ".env"


def test_config_prod():
    cfg = SettingsForTests()
    cfg_prod = Settings()
    assert len(cfg_prod.dict()) == len(cfg.dict())
