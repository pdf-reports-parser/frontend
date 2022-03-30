from frontend.schemas import Measurements


fake_measurements = [
    {
        'uid': 1,
        'measurement_object': 'Cherry Tiggo sert',
        'project': 'КИТАЙ',
        'report_date': '2032-04-23T10:20:30',
        'responsible_person': 'user',
    },
    {
        'uid': 2,
        'measurement_object': 'Toyota RAV4 sert',
        'project': 'ЯПОНИЯ',
        'report_date': '2032-04-23T10:20:30',
        'responsible_person': 'user',
    },
    {
        'uid': 3,
        'measurement_object': 'Audi Q6 sert',
        'project': 'ГЕРМАНИЯ',
        'report_date': '2032-04-23T10:20:30',
        'responsible_person': 'user',
    },
    {
        'uid': 4,
        'measurement_object': 'Honda Fit sert',
        'project': 'ЯПОНИЯ',
        'report_date': '2032-04-23T10:20:30',
        'responsible_person': 'user',
    },
    {
        'uid': 5,
        'measurement_object': 'VAZ 2106 sert',
        'project': 'РОССИИЯ',
        'report_date': '2032-04-23T10:20:30',
        'responsible_person': 'user',
    },
]


class MeasurementsClient:

    def __init__(self, url):
        self.url = f'{url}/measurements'

    def get_all(self):
        measurements = fake_measurements
        return [Measurements(**measurement) for measurement in measurements]
