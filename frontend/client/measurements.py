import httpx

from frontend.schemas import Measurements


fake_measurements = {
    "measurement_object": "Cherry Tiggo sert",
    "project": "КИТАЙ",
    "report_date": "Mon, 13 Dec 2021 15:29:00 GMT",
    "responsible_person": "user"
}


class MeasurementsClient:

    def __init__(self, url):
        self.url = f'{url}/measurements'

    def get_all(self):
        measurements = fake_measurements
        return [Measurements(**measurement) for measurement in measurements]
