import os

from pydantic import BaseModel


class AppConfig(BaseModel):
    backend_url: str
    app_host: str
    app_port: str


def load_from_env() -> AppConfig:
    backend_url = os.environ['BACKEND_URL']
    app_host = os.environ['APP_HOST']
    app_port = os.environ['APP_PORT']
    return AppConfig(
        backend_url=backend_url,
        app_host=app_host,
        app_port=app_port,
    )
