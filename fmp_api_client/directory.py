from typing import Literal

import asyncio

from fmp_api_client.base import Base
from fmp_api_client.plan import requires_plan, FMPPlan


class Directory(Base):
    @requires_plan(FMPPlan.STARTER)
    async def acompany_symbols_list(self) -> list[dict]:
        '''
        Easily retrieve a comprehensive list of financial symbols. 
        Access a broad range of stock symbols and other tradable financial instruments from various global exchanges, helping you explore the full range of available securities.
        '''
        endpoint = 'stock-list'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.STARTER)
    def company_symbols_list(self) -> list[dict]:
        return asyncio.run(self.acompany_symbols_list())
    
    @requires_plan(FMPPlan.STARTER)
    async def afinancial_statement_symbols_list(self) -> list[dict]:
        '''
        Access a comprehensive list of companies with available financial statements. 
        Find companies listed on major global exchanges and obtain up-to-date financial data including income statements, balance sheets, and cash flow statements, are provided.
        '''
        endpoint = 'financial-statement-symbol-list'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.STARTER)
    def financial_statement_symbols_list(self) -> list[dict]:
        return asyncio.run(self.afinancial_statement_symbols_list())
    
    @requires_plan(FMPPlan.STARTER)
    async def aCIK(self, limit: int | None = None) -> list[dict]:
        '''
        Access a comprehensive database of CIK (Central Index Key) numbers for SEC-registered entities. 
        This is essential for businesses, financial professionals, and individuals who need quick access to CIK numbers for regulatory compliance, financial transactions, and investment research.
        '''
        endpoint = 'cik-list'
        params = {}
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.STARTER)
    def CIK(self, limit: int | None = None) -> list[dict]:
        return asyncio.run(self.aCIK(limit))
    
    @requires_plan(FMPPlan.STARTER)
    async def asymbol_changes(
        self,
        invalid: bool=False,
        limit: int | None = None,
    ) -> list[dict]:
        '''
        Stay informed about the latest stock symbol changes. 
        Track changes due to mergers, acquisitions, stock splits, and name changes to ensure accurate trading and analysis.
        '''
        endpoint = 'symbol-change'
        params = {'invalid': invalid}
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.STARTER)
    def symbol_changes(
        self,
        invalid: bool=False,
        limit: int | None = None,
    ) -> list[dict]:
        return asyncio.run(self.asymbol_changes(invalid, limit))
    
    @requires_plan(FMPPlan.STARTER)
    async def aETF_symbol_search(self) -> list[dict]:
        '''
        Quickly find ticker symbols and company names for Exchange Traded Funds (ETFs). 
        This tool simplifies identifying specific ETFs by their name or ticker.
        '''
        endpoint = 'etf-list'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.STARTER)
    def ETF_symbol_search(self) -> list[dict]:
        return asyncio.run(self.aETF_symbol_search())
    
    @requires_plan(FMPPlan.STARTER)
    async def aactively_trading_list(self) -> list[dict]:
        '''
        List all actively trading companies and financial instruments. 
        This allows users to filter and display securities that are currently being traded on public exchanges, ensuring you access real-time market activity.
        '''
        endpoint = 'actively-trading-list'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.STARTER)
    def actively_trading_list(self) -> list[dict]:
        return asyncio.run(self.aactively_trading_list())
    
    @requires_plan(FMPPlan.STARTER)
    async def aearnings_transcript_list(self) -> list[dict]:
        '''
        Access available earnings transcripts for companies. 
        Retrieve a list of companies with earnings transcripts, along with the total number of transcripts available for each company.
        '''
        endpoint = 'earnings-transcript-list'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.STARTER)
    def earnings_transcript_list(self) -> list[dict]:
        return asyncio.run(self.aearnings_transcript_list())
    
    @requires_plan(FMPPlan.STARTER)
    async def aavailable_exchanges(self) -> list[dict[Literal['exchange'], str]]:
        '''
        Access a complete list of supported stock exchanges. 
        This provides a comprehensive overview of global stock exchanges, allowing users to identify where securities are traded and filter data by specific exchanges for further analysis.
        '''
        endpoint = 'available-exchanges'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.STARTER)
    def available_exchanges(self) -> list[dict[Literal['exchange'], str]]:
        return asyncio.run(self.aavailable_exchanges())
    
    @requires_plan(FMPPlan.STARTER)
    async def aavailable_sectors(self) -> list[dict[Literal['sector'], str]]:
        '''
        Access a complete list of industry sectors. 
        This helps users categorize and filter companies based on their respective sectors, enabling deeper analysis and more focused queries across different industries.
        '''
        endpoint = 'available-sectors'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.STARTER)
    def available_sectors(self) -> list[dict[Literal['sector'], str]]:
        return asyncio.run(self.aavailable_sectors())

    @requires_plan(FMPPlan.STARTER)
    async def aavailable_industries(self) -> list[dict[Literal['industry'], str]]:
        '''
        Access a comprehensive list of industries where stock symbols are available. 
        This helps users filter and categorize companies based on their industry for more focused research and analysis.
        '''
        endpoint = 'available-industries'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.STARTER)
    def available_industries(self) -> list[dict[Literal['industry'], str]]:
        return asyncio.run(self.aavailable_industries())
    
    @requires_plan(FMPPlan.STARTER)
    async def aavailable_countries(self) -> list[dict[Literal['country'], str]]:
        '''
        Access a comprehensive list of countries where stock symbols are available. 
        This enables users to filter and analyze stock symbols based on the country of origin or the primary market where the securities are traded.
        '''
        endpoint = 'available-countries'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.STARTER)
    def available_countries(self) -> list[dict[Literal['country'], str]]:
        return asyncio.run(self.aavailable_countries())
