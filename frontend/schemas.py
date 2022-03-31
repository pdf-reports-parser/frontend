from pydantic import BaseModel


class Measurement(BaseModel):

    uid: str
    name: str
    data: str
