import httpx

from frontend.schemas import Trial


class TrialsClient:
    def __init__(self, url: str) -> None:
        self.url = f'{url}'

    def get_for_measurement(self, measurement_id: int) -> list[Trial]:
        response = httpx.get(f'{self.url}/measurements/{measurement_id}/trials/')
        response.raise_for_status()

        trials = response.json()
        return [Trial(**trial) for trial in trials]
