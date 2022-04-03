import os

from pydantic import BaseModel


SECRET_KEY = 'HILUhik46846gfhbfgn6584968'

class AppConfig(BaseModel):
    backend_url: str
    app_host: str
    app_port: str
    debug: bool


def load_from_env() -> AppConfig:
    return AppConfig(
        backend_url=os.environ['BACKEND_URL'],
        app_host=os.environ['APP_HOST'],
        app_port=os.environ['APP_PORT'],
        debug=os.getenv('DEBUG', 'False')
    )


config = load_from_env()
