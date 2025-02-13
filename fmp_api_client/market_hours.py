import asyncio

from fmp_api_client.base import Base
from fmp_api_client.plan import FMPPlan, requires_plan


class MarketHours(Base):
    @requires_plan(FMPPlan.BASIC)
    async def amarket_hours(self, exchange: str='') -> list[dict]:
        '''
        Retrieve trading hours for specific stock exchanges if exchange is provided; if not, retrieve trading hours for all exchanges.
        '''
        if exchange:
            endpoint = 'exchange-market-hours'
        else:
            endpoint = 'all-exchange-market-hours'
        params = {}
        if exchange:
            params['exchange'] = exchange
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def market_hours(self, exchange: str='') -> list[dict]:
        return asyncio.run(self.amarket_hours(exchange))
