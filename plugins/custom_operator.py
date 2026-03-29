from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
import requests

class PolygonAPIToXComOperator(BaseOperator):

    @apply_defaults
    def __init__(self, api_key, ticker, **kwargs):
        super().__init__(**kwargs)
        self.api_key = api_key
        self.ticker = ticker

    def execute(self, context):
        ds = context.get("ds")

        url = f"https://api.polygon.io/v1/open-close/{self.ticker}/{ds}?adjusted=true&apiKey={self.api_key}"

        response = requests.get(url)
        data = response.json()

        return data   # goes to XCom automatically