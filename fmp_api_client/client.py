import os

import httpx


class FMPClient:
    _BASE_URL = 'https://financialmodelingprep.com/stable'
    
    
    def __init__(self, api_key: str | None = None):
        from fmp_api_client.search import Search
        from fmp_api_client.directory import Directory
        from fmp_api_client.analyst import Analyst
        self._api_key = api_key or os.getenv('FMP_API_KEY')
        assert self._api_key, 'FMP_API_KEY is not set'
        self.search = Search(self)
        self.directory = Directory(self)
        self.analyst = Analyst(self)

    async def _request(self, endpoint: str, params: dict | None = None, method: str='GET') -> dict | list | None:
        url = f'{self._BASE_URL}/{endpoint}'
        params = params or {}
        params['apikey'] = self._api_key
        async with httpx.AsyncClient() as client:
            try:
                response = await client.request(method, url, params=params)
                response.raise_for_status()
                return response.json()
            except httpx.RequestError as e:
                print(f"An error occurred while requesting {e.request.url!r}.")
            except httpx.HTTPStatusError as e:
                print(f"Error response {e.response.status_code} while requesting {e.request.url!r}.")


if __name__ == '__main__':
    from pprint import pprint
    client = FMPClient()
    res = client.analyst.stock_grade_latest_news(
        limit=100,
        symbol='BLK',
        # limit=10,
        # page=2,
        start_date='2025-01-29',
        end_date='2025-02-03',
    )
    pprint(res)