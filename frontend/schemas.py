from pydantic import BaseModel


class Measurements(BaseModel):

    uid: str
    name: str
    data: str
