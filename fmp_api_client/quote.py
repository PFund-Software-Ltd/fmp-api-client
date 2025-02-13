import asyncio

from fmp_api_client.base import Base
from fmp_api_client.plan import FMPPlan, requires_plan


class Quote(Base):
    @requires_plan(FMPPlan.BASIC)
    async def astock_quote(
        self, 
        symbol: str,
        # NOTE: custom params
        short: bool=True
    ) -> list[dict]:
        '''
        Access real-time stock quotes. 
        Get up-to-the-minute prices, changes, and volume data for individual stocks.
        '''
        if short:
            endpoint = 'quote-short'
        else:
            endpoint = 'quote'
        params = {'symbol': symbol}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def stock_quote(
        self, 
        symbol: str, 
        # NOTE: custom params
        short: bool=True
    ) -> list[dict]:
        return asyncio.run(self.astock_quote(symbol, short=short))
    
    @requires_plan(FMPPlan.BASIC)
    async def aaftermarket_trade(self, symbol: str) -> list[dict]:
        '''
        Track real-time trading activity occurring after regular market hours. 
        Access key details such as trade prices, sizes, and timestamps for trades executed during the post-market session.
        '''
        endpoint = 'aftermarket-trade'
        params = {'symbol': symbol}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def aftermarket_trade(self, symbol: str) -> list[dict]:
        return asyncio.run(self.aaftermarket_trade(symbol))
    
    @requires_plan(FMPPlan.BASIC)
    async def aaftermarket_quote(self, symbol: str) -> list[dict]:
        '''
        Access real-time aftermarket quotes for stocks. 
        Track bid and ask prices, volume, and other relevant data outside of regular trading hours.
        '''
        endpoint = 'aftermarket-quote'
        params = {'symbol': symbol}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def aftermarket_quote(self, symbol: str) -> list[dict]:
        return asyncio.run(self.aaftermarket_quote(symbol))
    
    @requires_plan(FMPPlan.BASIC)
    async def astock_price_change(self, symbol: str) -> list[dict]:
        '''
        Track stock price fluctuations in real-time. 
        Monitor percentage and value changes over various time periods, including daily, weekly, monthly, and long-term.
        '''
        endpoint = 'stock-price-change'
        params = {'symbol': symbol}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def stock_price_change(self, symbol: str) -> list[dict]:
        return asyncio.run(self.astock_price_change(symbol))
    
    @requires_plan(FMPPlan.BASIC)
    async def astock_batch_quote(
        self, 
        symbols: list[str],
        # NOTE: custom params
        short: bool=True
    ) -> list[dict]:
        '''
        Retrieve multiple real-time stock quotes in a single request. 
        Access current prices, volume, and detailed data for multiple companies at once, making it easier to track large portfolios or monitor multiple stocks simultaneously.
        '''
        if short:
            endpoint = 'batch-quote-short'
        else:
            endpoint = 'batch-quote'
        params = {'symbols': ','.join(symbols)}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def stock_batch_quote(
        self, 
        symbols: list[str],
        # NOTE: custom params
        short: bool=True
    ) -> list[dict]:
        return asyncio.run(self.astock_batch_quote(symbols, short=short))
    
    @requires_plan(FMPPlan.BASIC)
    async def abatch_aftermarket_trade(self, symbols: list[str]) -> list[dict]:
        '''
        Retrieve real-time aftermarket trading data for multiple stocks. 
        Track post-market trade prices, volumes, and timestamps across several companies simultaneously.
        '''
        endpoint = 'batch-aftermarket-trade'
        params = {'symbols': ','.join(symbols)}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def batch_aftermarket_trade(self, symbols: list[str]) -> list[dict]:
        return asyncio.run(self.abatch_aftermarket_trade(symbols))
    
    @requires_plan(FMPPlan.BASIC)
    async def abatch_aftermarket_quote(self, symbols: list[str]) -> list[dict]:
        '''
        Retrieve real-time aftermarket quotes for multiple stocks. 
        Access bid and ask prices, volume, and other relevant data for several companies during post-market trading.
        '''
        endpoint = 'batch-aftermarket-quote'
        params = {'symbols': ','.join(symbols)}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def batch_aftermarket_quote(self, symbols: list[str]) -> list[dict]:
        return asyncio.run(self.abatch_aftermarket_quote(symbols))
    
    @requires_plan(FMPPlan.BASIC)
    async def aexchange_stock_quotes(self, exchange: str, short: bool=True) -> list[dict]:
        '''
        Retrieve real-time stock quotes for all listed stocks on a specific exchange. 
        Track price changes and trading activity across the entire exchange.
        '''
        endpoint = 'batch-exchange-quote'
        params = {'exchange': exchange}
        if short:
            params['short'] = short
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def exchange_stock_quotes(self, exchange: str, short: bool=True) -> list[dict]:
        return asyncio.run(self.aexchange_stock_quotes(exchange, short))
    
    @requires_plan(FMPPlan.BASIC)
    async def amutual_fund_quotes(self, short: bool=True) -> list[dict]:
        '''
        Access real-time quotes for mutual funds. 
        Track current prices, performance changes, and key data for various mutual funds.
        '''
        endpoint = 'batch-mutualfund-quotes'
        params = {}
        if short:
            params['short'] = short
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def mutual_fund_quotes(self, short: bool=True) -> list[dict]:
        return asyncio.run(self.amutual_fund_quotes(short))
    
    @requires_plan(FMPPlan.BASIC)
    async def aETF_quotes(self, short: bool=True) -> list[dict]:
        '''
        Get real-time price quotes for exchange-traded funds (ETFs). 
        Track current prices, performance changes, and key data for a wide variety of ETFs.
        '''
        endpoint = 'batch-etf-quotes'
        params = {}
        if short:
            params['short'] = short
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def ETF_quotes(self, short: bool=True) -> list[dict]:
        return asyncio.run(self.aETF_quotes(short))
    
    @requires_plan(FMPPlan.BASIC)
    async def acommodity_quotes(self, short: bool=True) -> list[dict]:
        '''
        Get up-to-the-minute quotes for commodities. 
        Track the latest prices, changes, and volumes for a wide range of commodities, including oil, gold, and agricultural products.
        '''
        endpoint = 'batch-commodity-quotes'
        params = {}
        if short:
            params['short'] = short
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def commodity_quotes(self, short: bool=True) -> list[dict]:
        return asyncio.run(self.acommodity_quotes(short))
    
    @requires_plan(FMPPlan.BASIC)
    async def acrypto_quotes(self, short: bool=True) -> list[dict]:
        '''
        Access real-time cryptocurrency quotes. 
        Track live prices, trading volumes, and price changes for a wide range of digital assets.
        '''
        endpoint = 'batch-crypto-quotes'
        params = {}
        if short:
            params['short'] = short
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def crypto_quotes(self, short: bool=True) -> list[dict]:
        return asyncio.run(self.acrypto_quotes(short))
    
    @requires_plan(FMPPlan.BASIC)
    async def aforex_quotes(self, short: bool=True) -> list[dict]:
        '''
        Retrieve real-time quotes for multiple forex currency pairs. 
        Get real-time price changes and updates for a variety of forex pairs in a single request.
        '''
        endpoint = 'batch-forex-quotes'
        params = {}
        if short:
            params['short'] = short
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def forex_quotes(self, short: bool=True) -> list[dict]:
        return asyncio.run(self.aforex_quotes(short))
    
    @requires_plan(FMPPlan.BASIC)
    async def astock_index_quotes(self, short: bool=True) -> list[dict]:
        '''
        Track real-time movements of major stock market indexes. 
        Access live quotes for global indexes and monitor changes in their performance.
        '''
        endpoint = 'batch-index-quotes'
        params = {}
        if short:
            params['short'] = short
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def stock_index_quotes(self, short: bool=True) -> list[dict]:
        return asyncio.run(self.astock_index_quotes(short))
