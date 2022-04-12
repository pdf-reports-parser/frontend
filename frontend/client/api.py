from frontend.config import config
from frontend.client.measurements import MeasurementsClient
from frontend.client.trials import TrialsClient


class ApiClient:

    def __init__(self, url: str) -> None:
        self.measurements = MeasurementsClient(url)
        self.trials = TrialsClient(url)


client = ApiClient(url=config.backend_url)
