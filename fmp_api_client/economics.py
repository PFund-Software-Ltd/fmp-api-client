import asyncio

from fmp_api_client.base import Base
from fmp_api_client.plan import requires_plan, FMPPlan


class Economics(Base):
    @requires_plan(FMPPlan.BASIC)
    async def atreasury_rates(self, from_: str | None = None, to: str | None = None) -> list[dict]:
        '''
        Access real-time and historical Treasury rates for all maturities. 
        Track key benchmarks for interest rates across the economy.
        '''
        endpoint = 'treasury-rates'
        params = {}
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def treasury_rates(self, from_: str | None = None, to: str | None = None) -> list[dict]:
        return asyncio.run(self.atreasury_rates(from_, to))

    # TODO: find out options for "name", e.g. GDP, CPI, etc.
    @requires_plan(FMPPlan.BASIC)
    async def aeconomics_indicators(self, name: str, from_: str | None = None, to: str | None = None) -> list[dict]:
        '''
        Access real-time and historical economic data for key indicators like GDP, unemployment, and inflation. 
        Use this data to measure economic performance and identify growth trends.
        '''
        endpoint = 'economic-indicators'
        params = {'name': name}
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def economics_indicators(self, name: str, from_: str | None = None, to: str | None = None) -> list[dict]:
        return asyncio.run(self.aeconomics_indicators(name, from_, to))
    
    @requires_plan(FMPPlan.BASIC)
    async def aeconomic_data_releases_calendar(self, from_: str | None = None, to: str | None = None) -> list[dict]:
        '''
        Access a comprehensive calendar of upcoming economic data releases to prepare for market impacts and make informed investment decisions.
        '''
        endpoint = 'economic-calendar'
        params = {}
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def economic_data_releases_calendar(self, from_: str | None = None, to: str | None = None) -> list[dict]:
        return asyncio.run(self.aeconomic_data_releases_calendar(from_, to))

    @requires_plan(FMPPlan.BASIC)
    async def amarket_risk_premium(self) -> list[dict]:
        '''
        Access the market risk premium for specific dates. 
        Use this key financial metric to assess the additional return expected from investing in the stock market over a risk-free investment.
        '''
        endpoint = 'market-risk-premium'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def market_risk_premium(self) -> list[dict]:
        return asyncio.run(self.amarket_risk_premium())
