import httpx

from frontend import config
from frontend.schemas import Measurements

app_config = config.load_from_env()


class MeasurementsClient:

    def __init__(self, url=app_config.backend_url):
        self.url = f'{url}/measurements'

    def get_all(self):
        back_query = httpx.get(f'{self.url}/')
        measurements = back_query.json()
        return [Measurements(**measurement) for measurement in measurements]
