from fmp_api_client.client import FMPClient


class Base:
    def __init__(self, client: FMPClient):
        self._client = client
        self._request = client._request
