import asyncio

from fmp_api_client.base import Base
from fmp_api_client.plan import requires_plan, FMPPlan


class Company(Base):
    @requires_plan(FMPPlan.BASIC)
    async def acompany_profile_data(self, symbol: str) -> list[dict]:
        '''
        Access detailed company profile data. 
        This provides key financial and operational information for a specific stock symbol, including the company's market capitalization, stock price, industry, and much more.
        '''
        endpoint = 'profile'
        params = {'symbol': symbol}
        return await self._request(endpoint, params=params)
        
    @requires_plan(FMPPlan.BASIC)
    def company_profile_data(self, symbol: str) -> list[dict]:
        return asyncio.run(self.acompany_profile_data(symbol))
    
    @requires_plan(FMPPlan.BASIC)
    async def acompany_profile_by_CIK(self, cik: str) -> list[dict]:
        '''
        Retrieve detailed company profile data by CIK (Central Index Key). 
        This allows users to search for companies using their unique CIK identifier and access a full range of company data, including stock price, market capitalization, industry, and much more.
        '''
        endpoint = 'profile-cik'
        params = {'cik': cik}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def company_profile_by_CIK(self, cik: str) -> list[dict]:
        return asyncio.run(self.acompany_profile_by_CIK(cik))
    
    @requires_plan(FMPPlan.BASIC)
    async def acompany_notes(self, symbol: str) -> list[dict]:
        '''
        Retrieve detailed information about company-issued notes. 
        Access essential data such as CIK number, stock symbol, note title, and the exchange where the notes are listed.
        '''
        endpoint = 'company-notes'
        params = {'symbol': symbol}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def company_notes(self, symbol: str) -> list[dict]:
        return asyncio.run(self.acompany_notes(symbol))

    @requires_plan(FMPPlan.BASIC)
    async def astock_peer_comparison(self, symbol: str) -> list[dict]:
        '''
        Identify and compare companies within the same sector and market capitalization range. 
        Gain insights into how a company stacks up against its peers on the same exchange.
        '''
        endpoint = 'stock-peers'
        params = {'symbol': symbol}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def stock_peer_comparison(self, symbol: str) -> list[dict]:
        return asyncio.run(self.astock_peer_comparison(symbol))
    
    @requires_plan(FMPPlan.BASIC)
    async def adelisted_companies(self, limit: int | None = None, page: int | None = None) -> list[dict]:
        '''
        Access a comprehensive list of companies that have been delisted from US exchanges to avoid trading in risky stocks and identify potential financial troubles.
        '''
        endpoint = 'delisted-companies'
        params = {}
        if limit:
            params['limit'] = limit
        if page:
            params['page'] = page
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def delisted_companies(self, limit: int | None = None, page: int | None = None) -> list[dict]:
        return asyncio.run(self.adelisted_companies(limit, page))
    
    @requires_plan(FMPPlan.BASIC)
    async def acompany_employee_count(self, symbol: str, limit: int | None = None) -> list[dict]:
        '''
        Retrieve detailed workforce information for companies, including employee count, reporting period, and filing date.
        This also provides direct links to official SEC documents for further verification and in-depth research.
        '''
        endpoint = 'employee-count'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def company_employee_count(self, symbol: str, limit: int | None = None) -> list[dict]:
        return asyncio.run(self.acompany_employee_count(symbol, limit))
    
    @requires_plan(FMPPlan.BASIC)
    async def acompany_historical_employee_count(
        self, 
        symbol: str, 
        limit: int | None = None,
        page: int | None = None,
    ) -> list[dict]:
        '''
        Access historical employee count data for a company based on specific reporting periods. 
        This provides insights into how a company’s workforce has evolved over time, allowing users to analyze growth trends and operational changes.
        '''
        endpoint = 'historical-employee-count'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        if page:
            params['page'] = page
        return await self._request(endpoint, params=params)
    
    # REVIEW: the result of this endpoint is the same as company_employee_count()...
    @requires_plan(FMPPlan.BASIC)
    def company_historical_employee_count(
        self, 
        symbol: str, 
        limit: int | None = None, 
        page: int | None = None,
    ) -> list[dict]:
        return asyncio.run(self.acompany_historical_employee_count(symbol, limit, page))
    
    @requires_plan(FMPPlan.BASIC)
    async def acompany_market_cap(self, symbol: str) -> list[dict]:
        '''
        Retrieve the market capitalization for a specific company on any given date. 
        This provides essential data to assess the size and value of a company in the stock market, helping users gauge its overall market standing.
        '''
        endpoint = 'market-capitalization'
        params = {'symbol': symbol}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def company_market_cap(self, symbol: str) -> list[dict]:
        return asyncio.run(self.acompany_market_cap(symbol))
    
    @requires_plan(FMPPlan.BASIC)
    async def abatch_market_cap(self, symbols: list[str]) -> list[dict]:
        '''
        Retrieve market capitalization data for multiple companies in a single request. 
        This allows users to compare the market size of various companies simultaneously, streamlining the analysis of company valuations.
        '''
        endpoint = 'market-capitalization-batch'
        params = {'symbols': ','.join(symbols)}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def batch_market_cap(self, symbols: list[str]) -> list[dict]:
        return asyncio.run(self.abatch_market_cap(symbols))
    
    @requires_plan(FMPPlan.BASIC)
    async def ahistorical_market_cap(
        self, 
        symbol: str,
        limit: int | None = None,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[dict]:
        '''
        Access historical market capitalization data for a company. 
        This helps track the changes in market value over time, enabling long-term assessments of a company's growth or decline.
        '''
        endpoint = 'historical-market-capitalization'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def historical_market_cap(self, symbol: str, limit: int | None = None, from_: str | None = None, to: str | None = None) -> list[dict]:
        return asyncio.run(self.ahistorical_market_cap(symbol, limit, from_, to))

    @requires_plan(FMPPlan.BASIC)
    async def acompany_share_float_and_liquidity(self, symbol: str) -> list[dict]:
        '''
        Understand the liquidity and volatility of a stock. 
        Access the total number of publicly traded shares for any company to make informed investment decisions.
        '''
        endpoint = 'shares-float'
        params = {'symbol': symbol}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def company_share_float_and_liquidity(self, symbol: str) -> list[dict]:
        return asyncio.run(self.acompany_share_float_and_liquidity(symbol))
    
    @requires_plan(FMPPlan.BASIC)
    async def aall_shares_float(self) -> list[dict]:
        '''
        Access comprehensive shares float data for all available companies. 
        Retrieve critical information such as free float, float shares, and outstanding shares to analyze liquidity across a wide range of companies.
        '''
        endpoint = 'shares-float-all'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def all_shares_float(self) -> list[dict]:
        return asyncio.run(self.aall_shares_float())
    
    @requires_plan(FMPPlan.BASIC)
    async def alastest_mergers_and_acquisitions(self, page: int | None = None, limit: int | None = None) -> list[dict]:
        '''
        Access real-time data on the latest mergers and acquisitions. 
        This provides key information such as the transaction date, company names, and links to detailed filing information for further analysis.
        '''
        endpoint = 'mergers-acquisitions-latest'
        params = {}
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def latest_mergers_and_acquisitions(self, page: int | None = None, limit: int | None = None) -> list[dict]:
        return asyncio.run(self.alastest_mergers_and_acquisitions(page, limit))
    
    @requires_plan(FMPPlan.BASIC)
    async def asearch_mergers_and_acquisitions(self, name: str) -> list[dict]:
        '''
        Search for specific mergers and acquisitions data. 
        Retrieve detailed information on M&A activity, including acquiring and targeted companies, transaction dates, and links to official SEC filings.
        '''
        endpoint = 'mergers-acquisitions-search'
        params = {'name': name}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def search_mergers_and_acquisitions(self, name: str) -> list[dict]:
        return asyncio.run(self.asearch_mergers_and_acquisitions(name))
    
    @requires_plan(FMPPlan.BASIC)
    async def acompany_executives(self, symbol: str, active: bool=True) -> list[dict]:
        '''
        Retrieve detailed information on company executives. 
        This provides essential data about key executives, including their name, title, compensation, and other demographic details such as gender and year of birth.
        '''
        endpoint = 'key-executives'
        params = {'symbol': symbol, 'active': active}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def company_executives(self, symbol: str, active: bool=True) -> list[dict]:
        return asyncio.run(self.acompany_executives(symbol, active))
    
    @requires_plan(FMPPlan.BASIC)
    async def aexecutive_compensation(self, symbol: str) -> list[dict]:
        '''
        Retrieve comprehensive compensation data for company executives. 
        This provides detailed information on salaries, stock awards, total compensation, and other relevant financial data, including filing details and links to official documents.
        '''
        endpoint = 'governance-executive-compensation'
        params = {'symbol': symbol}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def executive_compensation(self, symbol: str) -> list[dict]:
        return asyncio.run(self.aexecutive_compensation(symbol))
    
    @requires_plan(FMPPlan.BASIC)
    async def aexecutive_compensation_benchmark(self, year: int | None = None) -> list[dict]:
        '''
        Gain access to average executive compensation data across various industries. 
        This provides essential insights for comparing executive pay by industry, helping you understand compensation trends and benchmarks.
        '''
        endpoint = 'executive-compensation-benchmark'
        params = {}
        if year:
            params['year'] = year
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def executive_compensation_benchmark(self, year: int | None = None) -> list[dict]:
        return asyncio.run(self.aexecutive_compensation_benchmark(year))
