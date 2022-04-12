from datetime import datetime

from pydantic import BaseModel


class Measurement(BaseModel):
    uid: int
    subject: str
    project: str
    date: datetime
    responsible: str


class Trial(BaseModel):
    uid: int
    name: str
    status: str
    unit: str
    value: str
    subject: str
    measure_id: int
