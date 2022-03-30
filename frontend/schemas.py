from datetime import datetime

from pydantic import BaseModel


class Measurements(BaseModel):

    measurement_object: str
    project: str
    report_date: datetime
    responsible_person: str
