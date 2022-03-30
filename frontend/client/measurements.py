import httpx

from frontend.schemas import Measurements


fake_measurements = [
    {
        "measurement_object": "Cherry Tiggo sert",
        "project": "КИТАЙ",
        "report_date": "2032-04-23T10:20:30",
        "responsible_person": "user"
    },
]


class MeasurementsClient:

    def __init__(self, url):
        self.url = f'{url}/measurements'

    def get_all(self):
        measurements = fake_measurements
        return [Measurements(**measurement) for measurement in measurements]
