import asyncio

from fmp_api_client.base import Base
from fmp_api_client.plan import FMPPlan, requires_plan


class MarketHours(Base):
    @requires_plan(FMPPlan.BASIC)
    async def aexchange_market_hours(self, exchange: str) -> list[dict]:
        '''
        Retrieve trading hours for specific stock exchanges. 
        Find out the opening and closing times of global exchanges to plan your trading strategies effectively.
        '''
        endpoint = 'exchange-market-hours'
        params = {'exchange': exchange}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def global_exchange_market_hours(self, exchange: str) -> list[dict]:
        return asyncio.run(self.aglobal_exchange_market_hours(exchange))

    @requires_plan(FMPPlan.BASIC)
    async def aall_exchange_market_hours(self) -> list[dict]:
        '''
        View the market hours for all exchanges. Check when different markets are active.
        '''
        endpoint = 'all-exchange-market-hours'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def all_exchange_market_hours(self) -> list[dict]:
        return asyncio.run(self.aall_exchange_market_hours())
