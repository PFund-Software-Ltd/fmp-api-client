import asyncio

from fmp_api_client.base import Base
from fmp_api_client.plan import FMPPlan, requires_plan


class MarketPerformance(Base):
    @requires_plan(FMPPlan.BASIC)
    async def amarket_sector_performance_snapshot(self, date: str, exchange: str = '', sector: str = '') -> list[dict]:
        '''
        Get a snapshot of sector performance. 
        Analyze how different industries are performing in the market based on average changes across sectors.
        '''
        endpoint = 'sector-performance-snapshot'
        params = {'date': date}
        if exchange:
            params['exchange'] = exchange
        if sector:
            params['sector'] = sector
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def market_sector_performance_snapshot(self, date: str, exchange: str = '', sector: str = '') -> list[dict]:
        return asyncio.run(self.amarket_sector_performance_snapshot(date, exchange, sector))
    
    @requires_plan(FMPPlan.BASIC)
    async def aindustry_performance_snapshot(self, date: str, exchange: str = '', industry: str = '') -> list[dict]:
        '''
        Access detailed performance data. 
        Analyze trends, movements, and daily performance metrics for specific industries across various stock exchanges.
        '''
        endpoint = 'industry-performance-snapshot'
        params = {'date': date}
        if exchange:
            params['exchange'] = exchange
        if industry:
            params['industry'] = industry
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def industry_performance_snapshot(self, date: str, exchange: str = '', industry: str = '') -> list[dict]:
        return asyncio.run(self.aindustry_performance_snapshot(date, exchange, industry))
    
    @requires_plan(FMPPlan.BASIC)
    async def ahistorical_market_sector_performance(self, sector: str, exchange: str = '', from_: str = '', to: str = '') -> list[dict]:
        '''
        Access historical sector performance data. 
        Review how different sectors have performed over time across various stock exchanges.
        '''
        endpoint = 'historical-sector-performance'
        params = {'sector': sector}
        if exchange:
            params['exchange'] = exchange
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def historical_market_sector_performance(self, sector: str, exchange: str = '', from_: str = '', to: str = '') -> list[dict]:
        return asyncio.run(self.ahistorical_market_sector_performance(sector, exchange, from_, to))
    
    @requires_plan(FMPPlan.BASIC)
    async def ahistorical_industry_performance(self, industry: str, exchange: str = '', from_: str = '', to: str = '') -> list[dict]:
        '''
        Access historical performance data for industries. 
        Track long-term trends and analyze how different industries have evolved over time across various stock exchanges.
        '''
        endpoint = 'historical-industry-performance'
        params = {'industry': industry}
        if exchange:
            params['exchange'] = exchange
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def historical_industry_performance(self, industry: str, exchange: str = '', from_: str = '', to: str = '') -> list[dict]:
        return asyncio.run(self.ahistorical_industry_performance(industry, exchange, from_, to))
    
    @requires_plan(FMPPlan.BASIC)
    async def asector_PE_snapshot(self,  date: str, exchange: str = '', sector: str = '') -> list[dict]:
        '''
        Retrieve the price-to-earnings (P/E) ratios for various sectors. 
        Compare valuation levels across sectors to better understand market valuations.
        '''
        endpoint = 'sector-pe-snapshot'
        params = {'date': date}
        if exchange:
            params['exchange'] = exchange
        if sector:
            params['sector'] = sector
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def sector_PE_snapshot(self, date: str, exchange: str = '', sector: str = '') -> list[dict]:
        return asyncio.run(self.asector_PE_snapshot(date, exchange, sector))
    
    @requires_plan(FMPPlan.BASIC)
    async def aindustry_PE_snapshot(self, date: str, exchange: str = '', industry: str = '') -> list[dict]:
        '''
        View price-to-earnings (P/E) ratios for different industries. 
        Analyze valuation levels across various industries to understand how each is priced relative to its earnings.
        '''
        endpoint = 'industry-pe-snapshot'
        params = {'date': date}
        if exchange:
            params['exchange'] = exchange
        if industry:
            params['industry'] = industry
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def industry_PE_snapshot(self, date: str, exchange: str = '', industry: str = '') -> list[dict]:
        return asyncio.run(self.aindustry_PE_snapshot(date, exchange, industry))
    
    @requires_plan(FMPPlan.BASIC)
    async def ahistorical_sector_PE(self, sector: str, exchange: str = '', from_: str = '', to: str = '') -> list[dict]:
        '''
        Access historical price-to-earnings (P/E) ratios for various sectors. 
        Analyze how sector valuations have evolved over time to understand long-term trends and market shifts.
        '''
        endpoint = 'historical-sector-pe'
        params = {'sector': sector}
        if exchange:
            params['exchange'] = exchange
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def historical_sector_PE(self, sector: str, exchange: str = '', from_: str = '', to: str = '') -> list[dict]:
        return asyncio.run(self.ahistorical_sector_PE(sector, exchange, from_, to))
    
    @requires_plan(FMPPlan.BASIC)
    async def ahistorical_industry_PE(self, industry: str, exchange: str = '', from_: str = '', to: str = '') -> list[dict]:
        '''
        Access historical price-to-earnings (P/E) ratios by industry. 
        Track valuation trends across various industries to understand how market sentiment and valuations have evolved over time.
        '''
        endpoint = 'historical-industry-pe'
        params = {'industry': industry}
        if exchange:
            params['exchange'] = exchange
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def historical_industry_PE(self, industry: str, exchange: str = '', from_: str = '', to: str = '') -> list[dict]:
        return asyncio.run(self.ahistorical_industry_PE(industry, exchange, from_, to))
    
    @requires_plan(FMPPlan.BASIC)
    async def abiggest_stock_gainers(self):
        '''
        Track the stocks with the largest price increases. 
        Identify the companies that are leading the market with significant price surges, offering potential growth opportunities.
        '''
        endpoint = 'biggest-gainers'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def biggest_stock_gainers(self):
        return asyncio.run(self.abiggest_stock_gainers())
    
    @requires_plan(FMPPlan.BASIC)
    async def abiggest_stock_losers(self):
        '''
        Access data on the stocks with the largest price drops. 
        Identify companies experiencing significant declines and track the stocks that are falling the fastest in the market.
        '''
        endpoint = 'biggest-losers'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def biggest_stock_losers(self):
        return asyncio.run(self.abiggest_stock_losers())
    
    @requires_plan(FMPPlan.BASIC)
    async def atop_traded_stocks(self):
        '''
        View the most actively traded stocks. 
        Identify the companies experiencing the highest trading volumes in the market and track where the most trading activity is happening.
        '''
        endpoint = 'most-actives'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def top_traded_stocks(self):
        return asyncio.run(self.atop_traded_stocks())
