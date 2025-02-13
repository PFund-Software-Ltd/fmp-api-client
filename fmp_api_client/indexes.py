from typing import Literal

import asyncio

from fmp_api_client.base import Base
from fmp_api_client.plan import FMPPlan, requires_plan


class Indexes(Base):
    @requires_plan(FMPPlan.BASIC)
    async def astock_market_indexes_list(self) -> list[dict]:
        '''
        Retrieve a comprehensive list of stock market indexes across global exchanges. 
        This provides essential information such as the symbol, name, exchange, and currency for each index, helping analysts and investors keep track of various market benchmarks.
        '''
        endpoint = 'index-list'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def stock_market_indexes_list(self) -> list[dict]:
        return asyncio.run(self.astock_market_indexes_list())
    
    @requires_plan(FMPPlan.BASIC)
    async def astock_index_quote(self, symbol: str) -> list[dict]:
        '''
        Access real-time stock index quotes. 
        Stay updated with the latest price changes, daily highs and lows, volume, and other key metrics for major stock indices around the world.
        '''
        endpoint = 'quote'
        params = {'symbol': symbol}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def stock_index_quote(self, symbol: str) -> list[dict]:
        return asyncio.run(self.astock_index_quote(symbol))
    
    @requires_plan(FMPPlan.BASIC)
    async def astock_index_short_quote(self, symbol: str) -> list[dict]:
        '''
        Access concise stock index quotes. 
        This provides a snapshot of the current price, change, and volume for stock indexes, making it ideal for users who need a quick overview of market movements.
        '''
        endpoint = 'quote-short'
        params = {'symbol': symbol}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def stock_index_short_quote(self, symbol: str) -> list[dict]:
        return asyncio.run(self.astock_index_short_quote(symbol))
    
    @requires_plan(FMPPlan.BASIC)
    async def aall_index_quotes(self, short: bool = True) -> list[dict]:
        '''
        The All Index Quotes API provides real-time quotes for a wide range of stock indexes, from major market benchmarks to niche indexes. 
        This allows users to track market performance across multiple indexes in a single request, giving them a broad view of the financial markets.
        '''
        endpoint = 'batch-index-quotes'
        params = {}
        if short:
            params['short'] = short
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def all_index_quotes(self, short: bool = True) -> list[dict]:
        return asyncio.run(self.aall_index_quotes(short))
    
    @requires_plan(FMPPlan.BASIC)
    async def ahistorical_stock_index_price_data(
        self, 
        symbol: str, 
        from_: str = '', 
        to: str = '',
        # NOTE: custom params
        short: bool = True,
    ) -> list[dict]:
        '''
        Retrieve end-of-day historical prices for stock indexes. 
        This provides essential data such as date, price, and volume, enabling detailed analysis of price movements over time.
        
        Args:
            symbol: index symbol, e.g. ^GSPC
        '''
        if short:
            endpoint = 'historical-price-eod/light'
        else:
            endpoint = 'historical-price-eod/full'
        params = {'symbol': symbol}
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def historical_stock_index_price_data(
        self, 
        symbol: str, 
        from_: str = '', 
        to: str = '', 
        # NOTE: custom params
        short: bool = True
    ) -> list[dict]:
        return asyncio.run(self.ahistorical_stock_index_price_data(symbol, from_, to, short))
    
    @requires_plan(FMPPlan.STARTER)
    async def astock_index_price_by_interval(
        self, 
        symbol: str, 
        from_: str = '', 
        to: str = '', 
        # NOTE: custom params
        interval: Literal['1min', '5min', '1hour'] = '1min',
    ) -> list[dict]:
        '''
        Retrieve 1-minute interval intraday data for stock indexes. 
        This provides granular price information, helping users track short-term price movements and trading volume within each minute.

        Args:
            symbol: index symbol, e.g. ^GSPC
        '''
        endpoint = f'historical-chart/{interval}'
        params = {'symbol': symbol}
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def stock_index_price_by_interval(
        self, 
        symbol: str, 
        from_: str = '', 
        to: str = '', 
        # NOTE: custom params
        interval: Literal['1min', '5min', '1hour'] = '1min'
    ) -> list[dict]:
        return asyncio.run(self.astock_index_price_by_interval(symbol, from_, to, interval))
    
    @requires_plan(FMPPlan.BASIC)
    async def aSP500_index_constituents(self) -> list[dict]:
        '''
        Access detailed data on the S&P 500 index. Track the performance and key information of the companies that make up this major stock market index.
        '''
        endpoint = 'sp500-constituent'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def SP500_index_constituents(self) -> list[dict]:
        return asyncio.run(self.aSP500_index_constituents())
    
    @requires_plan(FMPPlan.BASIC)
    async def aNASDAQ_index_constituents(self) -> list[dict]:
        '''
        Access comprehensive data for the Nasdaq index. 
        Monitor real-time movements and track the historical performance of companies listed on this prominent stock exchange.
        '''
        endpoint = 'nasdaq-constituent'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def NASDAQ_index_constituents(self) -> list[dict]:
        return asyncio.run(self.aNASDAQ_index_constituents())
    
    @requires_plan(FMPPlan.BASIC)
    async def aDow_Jones_index_constituents(self) -> list[dict]:
        '''
        Access data on the Dow Jones Industrial Average. 
        Track current values, analyze trends, and get detailed information about the companies that make up this important stock index.
        '''
        endpoint = 'dowjones-constituent'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def Dow_Jones_index_constituents(self) -> list[dict]:
        return asyncio.run(self.aDow_Jones_index_constituents())
    
    @requires_plan(FMPPlan.BASIC)
    async def ahistorical_SP500_constituents(self) -> list[dict]:
        '''
        Retrieve historical data for the S&P 500 index. 
        Analyze past changes in the index, including additions and removals of companies, to understand trends and performance over time.
        '''
        endpoint = 'historical-sp500-constituent'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def historical_SP500_constituents(self) -> list[dict]:
        return asyncio.run(self.ahistorical_SP500_constituents())
    
    @requires_plan(FMPPlan.BASIC)
    async def ahistorical_NASDAQ_constituents(self) -> list[dict]:
        '''
        Access historical data for the Nasdaq index. 
        Analyze changes in the index composition and view how it has evolved over time, including company additions and removals.
        '''
        endpoint = 'historical-nasdaq-constituent'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def historical_NASDAQ_constituents(self) -> list[dict]:
        return asyncio.run(self.ahistorical_NASDAQ_constituents())
    
    @requires_plan(FMPPlan.BASIC)
    async def ahistorical_Dow_Jones_constituents(self) -> list[dict]:
        '''
        Access historical data for the Dow Jones Industrial Average. 
        Analyze changes in the index’s composition and study its performance across different periods.
        '''
        endpoint = 'historical-dowjones-constituent'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def historical_Dow_Jones_constituents(self) -> list[dict]:
        return asyncio.run(self.ahistorical_Dow_Jones_constituents())
