import asyncio

from fmp_api_client.base import Base
from fmp_api_client.plan import FMPPlan, requires_plan


class InsiderTrades(Base):
    _base_endpoint = 'insider-trading'
    
    @requires_plan(FMPPlan.BASIC)
    async def alatest_insider_trading(
        self, 
        date: str = '',
        page: int | None = None,
        limit: int | None = None,
    ) -> list[dict]:
        '''
        Access the latest insider trading activity.
        Track which company insiders are buying or selling stocks and analyze their transactions.
        '''
        endpoint = f'{self._base_endpoint}/latest'
        params = {}
        if date:
            params['date'] = date
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def latest_insider_trading(
        self, 
        date: str = '',
        page: int | None = None,
        limit: int | None = None,
    ) -> list[dict]:
        return asyncio.run(self.alatest_insider_trading(date, page, limit))
    
    @requires_plan(FMPPlan.BASIC)
    async def asearch_insider_trades(
        self,
        symbol: str = '',
        page: int | None = None,
        limit: int | None = None,
        reportingCIK: str = '',
        companyCIK: str = '',
        transactionType: str = '',
    ) -> list[dict]:
        '''
        Search insider trading activity by company or symbol.
        Find specific trades made by corporate insiders, including executives and directors.
        '''
        endpoint = f'{self._base_endpoint}/search'
        params = {}
        if symbol:
            params['symbol'] = symbol
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit
        if reportingCIK:
            params['reportingCik'] = reportingCIK
        if companyCIK:
            params['companyCik'] = companyCIK
        if transactionType:
            params['transactionType'] = transactionType
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def search_insider_trades(
        self,
        symbol: str = '',
        page: int | None = None,
        limit: int | None = None,
        reportingCIK: str = '',
        companyCIK: str = '',
        transactionType: str = '',
    ) -> list[dict]:
        return asyncio.run(self.asearch_insider_trades(symbol, page, limit, reportingCIK, companyCIK, transactionType))
    
    @requires_plan(FMPPlan.BASIC)
    async def asearch_insider_trades_by_reporting_name(self, name: str) -> list[dict]:
        '''
        Search for insider trading activity by reporting name.
        Track trading activities of specific individuals or groups involved in corporate insider transactions.

        Args:
            name: e.g. Zuckerberg
        '''
        endpoint = f'{self._base_endpoint}/reporting-name'
        params = {'name': name}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def search_insider_trades_by_reporting_name(self, name: str) -> list[dict]:
        return asyncio.run(self.asearch_insider_trades_by_reporting_name(name))
    
    @requires_plan(FMPPlan.BASIC)
    async def aall_insider_transaction_types(self) -> list[dict]:
        '''
        Access a comprehensive list of insider transaction types. 
        This provides details on various transaction actions, including purchases, sales, and other corporate actions involving insider trading.
        '''
        endpoint = 'insider-trading-transaction-type'
        return await self._request(endpoint)
    
    @requires_plan(FMPPlan.BASIC)
    def all_insider_transaction_types(self) -> list[dict]:
        return asyncio.run(self.aall_insider_transaction_types())
    
    @requires_plan(FMPPlan.BASIC)
    async def ainsider_trade_statistics(self, symbol: str) -> list[dict]:
        '''
        Analyze insider trading activity. 
        This provides key statistics on insider transactions, including total purchases, sales, and trends for specific companies or stock symbols.
        '''
        endpoint = f'{self._base_endpoint}/statistics'
        params = {'symbol': symbol}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def insider_trade_statistics(self, symbol: str) -> list[dict]:
        return asyncio.run(self.ainsider_trade_statistics(symbol))

    @requires_plan(FMPPlan.BASIC)
    async def aacquisition_ownership(self, symbol: str, limit: int | None = None) -> list[dict]:
        '''
        Track changes in stock ownership during acquisitions.
        This provides detailed information on how mergers, takeovers, or beneficial ownership changes impact the stock ownership structure of a company.
        '''
        endpoint = f'{self._base_endpoint}/acquisition-ownership'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def acquisition_ownership(self, symbol: str, limit: int | None = None) -> list[dict]:
        return asyncio.run(self.aacquisition_ownership(symbol, limit))
