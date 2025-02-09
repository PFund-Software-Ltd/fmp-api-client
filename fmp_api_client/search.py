import asyncio

from fmp_api_client.base import Base
from fmp_api_client.plan import FMPPlan, requires_plan


class Search(Base):
    @requires_plan(FMPPlan.BASIC)
    async def astock_symbol(
        self, 
        query: str,
        limit: int | None = None,
        exchange: str = '',
    ) -> list[dict]:
        '''
        Search ticker symbol of any stock by company name or symbol across multiple global markets.
        
        Args:
            query: company name or symbol (e.g. AAPL)
            limit: number of results to return
            exchange: exchange name (e.g. NASDAQ)
        '''
        endpoint = 'search-symbol'
        params = {'query': query}
        if limit:
            params['limit'] = limit
        if exchange:
            params['exchange'] = exchange
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def stock_symbol(self, query: str, limit: int | None = None, exchange: str = '') -> list[dict]:
        return asyncio.run(self.astock_symbol(query, limit, exchange))
    
    @requires_plan(FMPPlan.BASIC)
    async def acompany_name(
        self,
        query: str,
        limit: int | None = None,
        exchange: str = '',
    ) -> list[dict]:
        '''
        Search for ticker symbols, company names, and exchange details for equity securities and ETFs listed on various exchanges
        This endpoint is useful for retrieving ticker symbols when you know the full or partial company or asset name but not the symbol identifier.
        '''
        endpoint = 'search-name'
        params = {'query': query}
        if limit:
            params['limit'] = limit
        if exchange:
            params['exchange'] = exchange
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)    
    def company_name(self, query: str, limit: int | None = None, exchange: str = '') -> list[dict]:
        return asyncio.run(self.acompany_name(query, limit, exchange))

    @requires_plan(FMPPlan.BASIC)
    async def aCIK(
        self,
        cik: str,
        limit: int | None = None,
    ) -> list[dict]:
        '''
        Retrieve the Central Index Key (CIK) for publicly traded companies.
        Access unique identifiers needed for SEC filings and regulatory documents for a streamlined compliance and financial analysis process. 
        '''
        endpoint = 'search-cik'
        params = {'cik': cik}
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def CIK(self, cik: str, limit: int | None = None) -> list[dict]:
        return asyncio.run(self.aCik(cik, limit))
    
    @requires_plan(FMPPlan.BASIC)  
    async def aCUSIP(self, cusip: str) -> list[dict]:
        '''
        Search and retrieve financial securities information by CUSIP number.
        Find key details such as company name, stock symbol, and market capitalization associated with the CUSIP.
        '''
        endpoint = 'search-cusip'
        params = {'cusip': cusip}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def CUSIP(self, cusip: str) -> list[dict]:
        return asyncio.run(self.aCUSIP(cusip))
    
    @requires_plan(FMPPlan.BASIC)
    async def aISIN(self, isin: str) -> list[dict]:
        '''
        search and retrieve the International Securities Identification Number (ISIN) for financial securities. 
        Find key details such as company name, stock symbol, and market capitalization associated with the ISIN.
        '''
        endpoint = 'search-isin'
        params = {'isin': isin}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def ISIN(self, isin: str) -> list[dict]:
        return asyncio.run(self.aISIN(isin))
    
    # TODO: find out the supported values for e.g. sector, industry, etc.
    @requires_plan(FMPPlan.BASIC)
    async def astock_screener(
        self,
        marketCapMoreThan: int | None = None,
        marketCapLowerThan: int | None = None,
        sector: str | None = None,
        industry: str | None = None,
        betaMoreThan: float | None = None,
        betaLowerThan: float | None = None,
        priceMoreThan: int | None = None,
        priceLowerThan: int | None = None,
        dividendMoreThan: float | None = None,
        dividendLowerThan: float | None = None,
        volumeMoreThan: int | None = None,
        volumeLowerThan: int | None = None,
        exchange: str | None = None,
        country: str | None = None,
        isEtf: bool | None = None,
        isFund: bool | None = None,
        isActivelyTrading: bool | None = None,
        limit: int | None = None,
        includeAllShareClasses: bool | None = None,
    ) -> list[dict]:
        '''
        Discover stocks that align with your investment strategy. 
        Filter stocks based on market cap, price, volume, beta, sector, country, and more to identify the best opportunities.
        '''
        endpoint = 'company-screener'
        params = {k: v for k, v in locals().items() if v is not None and k not in ('self', 'endpoint')}
        return await self._request(endpoint, params=params)
        
    @requires_plan(FMPPlan.BASIC)
    def stock_screener(
        self,
        marketCapMoreThan: int | None = None,
        marketCapLowerThan: int | None = None,
        sector: str | None = None,
        industry: str | None = None,
        betaMoreThan: float | None = None,
        betaLowerThan: float | None = None,
        priceMoreThan: int | None = None,
        priceLowerThan: int | None = None,
        dividendMoreThan: float | None = None,
        dividendLowerThan: float | None = None,
        volumeMoreThan: int | None = None,
        volumeLowerThan: int | None = None,
        exchange: str | None = None,
        country: str | None = None,
        isEtf: bool | None = None,
        isFund: bool | None = None,
        isActivelyTrading: bool | None = None,
        limit: int | None = None,
        includeAllShareClasses: bool | None = None,
    ) -> list[dict]:
        params = {k: v for k, v in locals().items() if k != 'self'}
        return asyncio.run(self.astock_screener(**params))

    # NOTE: despite the name, this is actually useful to get a company's:
    # description, logo image, CEO, market cap, price, beta, cik, isin, cusip, industry, sector, website, number of employees
    @requires_plan(FMPPlan.BASIC)
    async def aexchange_variants(self, symbol: str) -> list[dict]:
        '''
        Search across multiple public exchanges to find where a given stock symbol is listed. 
        This allows users to quickly identify all the exchanges where a security is actively traded.
        '''
        endpoint = 'search-exchange-variants'
        params = {'symbol': symbol}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)    
    def exchange_variants(self, symbol: str) -> list[dict]:
        return asyncio.run(self.aexchange_variants(symbol))
