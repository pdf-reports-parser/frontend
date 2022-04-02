import httpx

from frontend import config
from frontend.schemas import Measurement

app_config = config.load_from_env()


class MeasurementsClient:

    def __init__(self, url=app_config.backend_url):
        self.url = f'{url}/measurements'

    def get_all(self) -> list[Measurement]:
        back_query = httpx.get(f'{self.url}/')
        measurements = back_query.json()
        return [Measurement(**measurement) for measurement in measurements]

    def get_by_id(self, uid: int) -> Measurement:
        back_query = httpx.get(f'{self.url}/{uid}')
        return Measurement(**back_query.json())
