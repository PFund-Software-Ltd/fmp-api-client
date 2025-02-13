import os

import httpx

from fmp_api_client.search import Search
from fmp_api_client.directory import Directory
from fmp_api_client.analyst import Analyst
from fmp_api_client.news import News
from fmp_api_client.company import Company
from fmp_api_client.calendar import Calendar
from fmp_api_client.economics import Economics
from fmp_api_client.statements import Statements
from fmp_api_client.market_performance import MarketPerformance
from fmp_api_client.quote import Quote
from fmp_api_client.market_hours import MarketHours
from fmp_api_client.discounted_cashflow import DiscountedCashflow
from fmp_api_client.insider_trades import InsiderTrades
from fmp_api_client.indexes import Indexes


class FMPClient:
    _BASE_URL = 'https://financialmodelingprep.com/stable'
    
    def __init__(self, api_key: str | None = None):
        self._api_key = api_key or os.getenv('FMP_API_KEY') or os.getenv('FINANCIAL_MODELING_PREP_API_KEY')
        assert self._api_key, 'FMP_API_KEY or FINANCIAL_MODELING_PREP_API_KEYis not set'
        self.search = Search(self)
        self.directory = Directory(self)
        self.analyst = Analyst(self)
        self.calendar = Calendar(self)
        self.company = Company(self)
        self.news = News(self)
        self.economics = Economics(self)
        self.statements = Statements(self)
        self.market_performance = MarketPerformance(self)
        self.market_hours = MarketHours(self)
        self.insider_trades = InsiderTrades(self)
        self.indexes = Indexes(self)
        self.quote = Quote(self)
        self.discounted_cashflow = DiscountedCashflow(self)
        
    async def _request(self, endpoint: str, params: dict | None = None, method: str='GET') -> dict | list | None:
        url = f'{self._BASE_URL}/{endpoint}'
        params = params or {}
        params['apikey'] = self._api_key
        async with httpx.AsyncClient() as client:
            try:
                response = await client.request(method, url, params=params)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 402:
                    print(e.response.text)
                else:
                    print(f"Error response {e.response.status_code} while requesting {e.request.url!r}.")
            except httpx.RequestError as e:
                print(f"An error occurred while requesting {e.request.url!r}.")
