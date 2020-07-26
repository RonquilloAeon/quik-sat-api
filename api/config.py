from pydantic import BaseSettings


class Config(BaseSettings):
    SATELLITE_REPOSITORY_URL: str

    class Config:
        case_sensitive = True
