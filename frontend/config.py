import os

from pydantic import BaseModel


class AppConfig(BaseModel):
    endpoint: str
    host: str
    port: str


def load_from_env() -> AppConfig:
    endpoint = os.environ['ENDPOINT']
    host = os.environ['HOST']
    port = os.environ['PORT']
    return AppConfig(
        endpoint=endpoint,
        host=host,
        port=port,
    )