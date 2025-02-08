import datetime

from fmp_api_client.client import FMPClient


class Base:
    def __init__(self, client: FMPClient):
        self._client = client
        self._request = client._request

    def _prepare_dates(self, start_date: str, end_date: str) -> tuple[datetime.datetime, datetime.datetime]:
        if start_date:
            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d') 
        else:
            start_date = datetime.datetime.min
        if end_date:
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        else:
            end_date = datetime.datetime.max
        return start_date, end_date