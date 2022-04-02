import httpx

from frontend.config import config
from frontend.client.schemas import Measurement


class MeasurementsClient:

    def __init__(self, url: str) -> None:
        self.url = f'{url}/measurements'

    def get_all(self) -> list[Measurement]:
        response = httpx.get(f'{self.url}/')
        response.raise_for_status()

        measurements = response.json()
        return [Measurement(**measurement) for measurement in measurements]

    def get_by_id(self, uid: int) -> Measurement:
        response = httpx.get(f'{self.url}/{uid}')
        response.raise_for_status()

        payload = response.json()
        return Measurement(**payload)


client = MeasurementsClient(url=config.backend_url)
