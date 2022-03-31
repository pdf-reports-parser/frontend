from pydantic import BaseModel


class Measurement(BaseModel):

    uid: str
    measurement_object: str
    project: str
    report_date: str
    responsible_person: str
