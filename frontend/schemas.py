from datetime import datetime

from pydantic import BaseModel


class Measurement(BaseModel):

    uid: int
    measurement_object: str
    project: str
    report_date: datetime
    responsible_person: str
