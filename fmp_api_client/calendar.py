import asyncio

from fmp_api_client.base import Base
from fmp_api_client.plan import requires_plan, FMPPlan


class Calendar(Base):
    @requires_plan(FMPPlan.BASIC)
    async def adividends_company(
        self, 
        symbol: str,
        limit: int | None = None,
    ) -> list[dict]:
        '''
        Stay informed about upcoming dividend payments. 
        This provides essential dividend data for individual stock symbols, including record dates, payment dates, declaration dates, and more.
        '''
        endpoint = 'dividends'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)

    @requires_plan(FMPPlan.BASIC)
    def dividends_company(self, symbol: str, limit: int | None = None) -> list[dict]:
        return asyncio.run(self.adividends_company(symbol, limit=limit))
    
    @requires_plan(FMPPlan.BASIC)
    async def adividends_calendar(
        self,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[dict]:
        '''
        Stay informed on upcoming dividend events. 
        Access a comprehensive schedule of dividend-related dates for all stocks, including record dates, payment dates, declaration dates, and dividend yields.
        '''
        endpoint = 'dividends-calendar'
        params = {}
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def dividends_calendar(self, from_: str | None = None, to: str | None = None) -> list[dict]:
        return asyncio.run(self.adividends_calendar(from_, to))
    
    @requires_plan(FMPPlan.BASIC)
    async def aearnings_report(
        self, 
        symbol: str,
        limit: int | None = None,
    ) -> list[dict]:
        '''
        Retrieve in-depth earnings information. 
        Gain access to key financial data for a specific stock symbol, including earnings report dates, EPS estimates, and revenue projections to help you stay on top of company performance.
        '''
        endpoint = 'earnings'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def earnings_report(self, symbol: str, limit: int | None = None) -> list[dict]:
        return asyncio.run(self.aearnings_report(symbol, limit=limit))
    
    @requires_plan(FMPPlan.BASIC)
    async def aIPOs_calendar(
        self,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[dict]:
        '''
        Access a comprehensive list of all upcoming initial public offerings (IPOs). 
        Stay up to date on the latest companies entering the public market, with essential details on IPO dates, company names, expected pricing, and exchange listings.
        '''
        endpoint = 'ipos-calendar'
        params = {}
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def IPOs_calendar(self, from_: str | None = None, to: str | None = None) -> list[dict]:
        return asyncio.run(self.aIPOs_calendar(from_, to))
    
    @requires_plan(FMPPlan.BASIC)
    async def aIPOs_disclosure(
        self,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[dict]:
        '''
        Access a comprehensive list of disclosure filings for upcoming initial public offerings (IPOs). 
        Stay updated on regulatory filings, including filing dates, effectiveness dates, CIK numbers, and form types, with direct links to official SEC documents.
        '''
        endpoint = 'ipos-disclosure'
        params = {}
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def IPOs_disclosure(self, from_: str | None = None, to: str | None = None) -> list[dict]:
        return asyncio.run(self.aIPOs_disclosure(from_, to))
    
    @requires_plan(FMPPlan.BASIC)
    async def aIPOs_prospectus(
        self,
        from_: str | None = None,
        to: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[dict]:
        '''
        Access comprehensive information on IPO prospectuses. 
        Get key financial details, such as public offering prices, discounts, commissions, proceeds before expenses, and more. 
        This also provides links to official SEC prospectuses, helping investors stay informed on companies entering the public market.
        '''
        endpoint = 'ipos-prospectus'
        params = {}
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def IPOs_prospectus(self, from_: str | None = None, to: str | None = None, page: int | None = None, limit: int | None = None) -> list[dict]:
        return asyncio.run(self.aIPOs_prospectus(from_, to, page, limit))
    
    @requires_plan(FMPPlan.BASIC)
    async def astock_split_details(
        self,
        symbol: str,
        limit: int | None = None,
    ) -> list[dict]:
        '''
        Access detailed information on stock splits for a specific company. 
        This provides essential data, including the split date and the split ratio, helping users understand changes in a company's share structure after a stock split.
        '''
        endpoint = 'splits'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def stock_split_details(self, symbol: str, limit: int | None = None) -> list[dict]:
        return asyncio.run(self.astock_split_details(symbol, limit=limit))
    
    @requires_plan(FMPPlan.BASIC)
    async def astock_splits_calendar(
        self,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[dict]:
        '''
        Stay informed about upcoming stock splits. 
        This provides essential data on upcoming stock splits across multiple companies, including the split date and ratio, helping you track changes in share structures before they occur.
        '''
        endpoint = 'splits-calendar'
        params = {}
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def stock_splits_calendar(self, from_: str | None = None, to: str | None = None) -> list[dict]:
        return asyncio.run(self.astock_splits_calendar(from_, to))
        