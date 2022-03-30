from frontend import config
from frontend.client.measurements import MeasurementsClient

app_config = config.load_from_env()
endpoint = app_config.endpoint

measurements_client = MeasurementsClient(endpoint)

__all__ = ['measurements_client']
