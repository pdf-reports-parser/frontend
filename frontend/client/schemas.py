from datetime import datetime

from pydantic import BaseModel


class Measurement(BaseModel):
    uid: int
    subject: str
    project: str
    date: datetime
    responsible: str
