from typing import Literal

import asyncio

from fmp_api_client.base import Base
from fmp_api_client.plan import requires_plan, FMPPlan


class Statements(Base):
    # TODO: find out supported values of "period"
    @requires_plan(FMPPlan.BASIC)
    async def areal_time_income_statements(
        self, 
        symbol: str,
        limit: int | None = None,
        period: str | None = None,  
    ) -> list[dict]:
        '''
        Access real-time income statement data for public companies, private companies, and ETFs. 
        Track profitability, compare competitors, and identify business trends with up-to-date financial data.
        
        Args:
            period: e.g. FY
        '''
        endpoint = 'income-statement'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        if period:
            params['period'] = period
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def real_time_income_statements(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        return asyncio.run(self.areal_time_income_statements(symbol, limit, period))
    
    @requires_plan(FMPPlan.BASIC)
    async def abalance_sheet_data(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        '''
        Access detailed balance sheet statements for publicly traded companies. 
        Analyze assets, liabilities, and shareholder equity to gain insights into a company's financial health.
        '''    
        endpoint = 'balance-sheet-statement'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        if period:
            params['period'] = period
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def balance_sheet_data(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        return asyncio.run(self.abalance_sheet_data(symbol, limit, period))
    
    @requires_plan(FMPPlan.BASIC)
    async def acash_flow_statements(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        '''
        Gain insights into a company's cash flow activities. 
        Analyze cash generated and used from operations, investments, and financing activities to evaluate the financial health and sustainability of a business.
        '''
        endpoint = 'cash-flow-statement'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        if period:
            params['period'] = period
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def cash_flow_statements(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        return asyncio.run(self.acash_flow_statements(symbol, limit, period))
    
    @requires_plan(FMPPlan.ULTIMATE)
    async def alatest_financial_statements(self) -> list[dict]:
        endpoint = 'latest-financial-statements'
        params = {}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.ULTIMATE)
    def latest_financial_statements(self) -> list[dict]:
        return asyncio.run(self.alatest_financial_statements())
    
    @requires_plan(FMPPlan.ULTIMATE)
    async def aincome_statements(self, symbol: str, limit: int | None = None) -> list[dict]:
        endpoint = 'income-statement-ttm'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.ULTIMATE)
    def income_statements(self, symbol: str, limit: int | None = None) -> list[dict]:
        return asyncio.run(self.aincome_statements(symbol, limit))
    
    @requires_plan(FMPPlan.ULTIMATE)
    async def abalance_sheet_statements_TTM(self, symbol: str, limit: int | None = None) -> list[dict]:
        endpoint = 'balance-sheet-statement-ttm'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.ULTIMATE)
    def balance_sheet_statements_TTM(self, symbol: str, limit: int | None = None) -> list[dict]:
        return asyncio.run(self.abalance_sheet_statements_TTM(symbol, limit))
    
    @requires_plan(FMPPlan.ULTIMATE)
    async def acash_flow_statements_TTM(self, symbol: str, limit: int | None = None) -> list[dict]:
        endpoint = 'cash-flow-statement-ttm'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.ULTIMATE)
    def cash_flow_statements_TTM(self, symbol: str, limit: int | None = None) -> list[dict]:
        return asyncio.run(self.acash_flow_statements_TTM(symbol, limit))
    
    @requires_plan(FMPPlan.BASIC)
    async def akey_metrics(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        '''
        Access essential financial metrics for a company. 
        Evaluate revenue, net income, P/E ratio, and more to assess performance and compare it to competitors.
        '''
        endpoint = 'key-metrics'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        if period:
            params['period'] = period
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def key_metrics(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        return asyncio.run(self.akey_metrics(symbol, limit, period))
    
    @requires_plan(FMPPlan.BASIC)
    async def afinancial_ratios(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        '''
        Analyze a company's financial performance. 
        This provides detailed profitability, liquidity, and efficiency ratios, enabling users to assess a company's operational and financial health across various metrics.
        '''
        endpoint = 'ratios'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        if period:
            params['period'] = period
        return await self._request(endpoint, params=params)

    @requires_plan(FMPPlan.BASIC)
    def financial_ratios(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        return asyncio.run(self.afinancial_ratios(symbol, limit, period))
    
    @requires_plan(FMPPlan.BASIC)
    async def akey_metrics_TTM(self, symbol: str, limit: int | None = None) -> list[dict]:
        endpoint = 'key-metrics-ttm'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def key_metrics_TTM(self, symbol: str, limit: int | None = None) -> list[dict]:
        return asyncio.run(self.akey_metrics_TTM(symbol, limit))
    
    @requires_plan(FMPPlan.BASIC)
    async def aTTM_ratios(self, symbol: str, limit: int | None = None) -> list[dict]:
        '''
        Gain access to trailing twelve-month (TTM) financial ratios. 
        This provides key performance metrics over the past year, including profitability, liquidity, and efficiency ratios.
        '''
        endpoint = 'ratios-ttm'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def TTM_ratios(self, symbol: str, limit: int | None = None) -> list[dict]:
        return asyncio.run(self.aTTM_ratios(symbol, limit))
    
    @requires_plan(FMPPlan.BASIC)
    async def afinancial_scores(self, symbol: str, limit: int | None = None) -> list[dict]:
        '''
        Assess a company's financial strength. 
        This provides key metrics such as the Altman Z-Score and Piotroski Score, giving users insights into a company’s overall financial health and stability.
        '''
        endpoint = 'financial-scores'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def financial_scores(self, symbol: str, limit: int | None = None) -> list[dict]:
        return asyncio.run(self.afinancial_scores(symbol, limit))
    
    @requires_plan(FMPPlan.BASIC)
    async def aowner_earnings(self, symbol: str, limit: int | None = None) -> list[dict]:
        '''
        Retrieve a company's owner earnings. 
        This provides a more accurate representation of cash available to shareholders by adjusting net income. 
        This metric is crucial for evaluating a company’s profitability from the perspective of investors.
        '''
        endpoint = 'owner-earnings'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def owner_earnings(self, symbol: str, limit: int | None = None) -> list[dict]:
        return asyncio.run(self.aowner_earnings(symbol, limit))
    
    # TODO: find out supported values of "period"
    @requires_plan(FMPPlan.BASIC)
    async def aenterprise_values(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        '''
        Access a company's enterprise value. 
        This metric offers a comprehensive view of a company's total market value by combining both its equity (market capitalization) and debt, providing a better understanding of its worth.
        
        Args:
            period: e.g. annual
        '''
        endpoint = 'enterprise-values'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        if period:
            params['period'] = period
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def enterprise_values(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        return asyncio.run(self.aenterprise_values(symbol, limit, period))
    

    @requires_plan(FMPPlan.BASIC)
    async def aincome_statement_growth(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        '''
        Track key financial growth metrics. 
        Analyze how revenue, profits, and expenses have evolved over time, offering insights into a company’s financial health and operational efficiency.
        
        Args:
            period: e.g. FY
        '''
        endpoint = 'income-statement-growth'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        if period:
            params['period'] = period
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def income_statement_growth(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        return asyncio.run(self.aincome_statement_growth(symbol, limit, period))
    
    @requires_plan(FMPPlan.BASIC)
    async def abalance_sheet_statement_growth(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        '''
        Analyze the growth of key balance sheet items over time. 
        Track changes in assets, liabilities, and equity to understand the financial evolution of a company.
        
        Args:
            period: e.g. FY
        '''
        endpoint = 'balance-sheet-statement-growth'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        if period:
            params['period'] = period
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def balance_sheet_statement_growth(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        return asyncio.run(self.abalance_sheet_statement_growth(symbol, limit, period))
    
    @requires_plan(FMPPlan.BASIC)
    async def acashflow_statement_growth(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        '''
        Measure the growth rate of a company’s cash flow. 
        Determine how quickly a company’s cash flow is increasing or decreasing over time.
        
        Args:
            period: e.g. FY
        '''
        endpoint = 'cashflow-statement-growth'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        if period:
            params['period'] = period
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def cashflow_statement_growth(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        return asyncio.run(self.acashflow_statement_growth(symbol, limit, period))
    
    @requires_plan(FMPPlan.BASIC)
    async def afinancial_statement_growth(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        '''
        Analyze the growth of key financial statement items across income, balance sheet, and cash flow statements. 
        Track changes over time to understand trends in financial performance.
        
        Args:
            period: e.g. FY
        '''
        endpoint = 'financial-growth'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        if period:
            params['period'] = period
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def financial_statement_growth(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        return asyncio.run(self.afinancial_statement_growth(symbol, limit, period))
    
    @requires_plan(FMPPlan.BASIC)
    async def afinancial_reports_form_10k(self, symbol: str, year: int, period: str='FY', format: Literal['json', 'xlsx']='json') -> list[dict]:
        '''
        Access comprehensive annual reports. 
        Obtain detailed information about a company’s financial performance, business operations, and risk factors as reported to the SEC.
        '''
        format = format.lower()
        if format == 'json':
            endpoint = 'financial-reports-json'
        elif format == 'xlsx':
            endpoint = 'financial-reports-xlsx'
        else:
            raise ValueError(f'Invalid format: {format}')
        params = {'symbol': symbol, 'year': year, 'period': period}
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def financial_reports_form_10k(self, symbol: str, year: int, period: str='FY', format: Literal['json', 'xlsx']='json') -> list[dict]:
        return asyncio.run(self.afinancial_reports_form_10k(symbol, year, period=period, format=format))

    # TODO: find out supported values of "period" and "structure"
    @requires_plan(FMPPlan.BASIC)
    async def arevenue_product_segmentation(self, symbol: str, period: int | None = None, structure: str | None = None) -> list[dict]:
        '''
        Access detailed revenue breakdowns by product line. 
        Understand which products drive a company's earnings and get insights into the performance of individual product segments.
        
        Args:
            period: e.g. annual
            structure: e.g. flat
        '''
        endpoint = 'revenue-product-segmentation'
        params = {'symbol': symbol}
        if period:
            params['period'] = period
        if structure:
            params['structure'] = structure
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def revenue_product_segmentation(self, symbol: str, period: int | None = None, structure: str | None = None) -> list[dict]:
        return asyncio.run(self.arevenue_product_segmentation(symbol, period, structure))
    
    # TODO: find out supported values of "period" and "structure"
    @requires_plan(FMPPlan.BASIC)
    async def arevenue_geographic_segmentation(self, symbol: str, period: int | None = None, structure: str | None = None) -> list[dict]:
        '''
        Access detailed revenue breakdowns by geographic region. 
        Analyze how different regions contribute to a company’s total revenue and identify key markets for growth.
        
        Args:
            period: e.g. annual
            structure: e.g. flat
        '''
        endpoint = 'revenue-geographic-segmentation'
        params = {'symbol': symbol}
        if period:
            params['period'] = period
        if structure:
            params['structure'] = structure
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def revenue_geographic_segmentation(self, symbol: str, period: int | None = None, structure: str | None = None) -> list[dict]:
        return asyncio.run(self.arevenue_geographic_segmentation(symbol, period, structure))
    
    @requires_plan(FMPPlan.BASIC)
    async def aas_reported_income_statements(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        '''
        Retrieve income statements as they were reported by the company. 
        Access raw financial data directly from official company filings, including revenue, expenses, and net income.
        
        Args:
            period: e.g. annual
        '''
        endpoint = 'income-statement-as-reported'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        if period:
            params['period'] = period
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def as_reported_income_statements(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        return asyncio.run(self.aas_reported_income_statements(symbol, limit, period))
    
    @requires_plan(FMPPlan.BASIC)
    async def aas_reported_balance_statements(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        '''
        Access balance sheets as reported by the company. 
        View detailed financial data on assets, liabilities, and equity directly from official filings.
        
        Args:
            period: e.g. annual
        '''
        endpoint = 'balance-sheet-statement-as-reported'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        if period:
            params['period'] = period
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def as_reported_balance_statements(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        return asyncio.run(self.aas_reported_balance_statements(symbol, limit, period))
    
    @requires_plan(FMPPlan.BASIC)
    async def aas_reported_cashflow_statements(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        '''
        View cash flow statements as reported by the company. 
        Analyze a company's cash flows related to operations, investments, and financing directly from official reports.
        
        Args:
            period: e.g. annual
        '''
        endpoint = 'cash-flow-statement-as-reported'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        if period:
            params['period'] = period
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def as_reported_cashflow_statements(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        return asyncio.run(self.aas_reported_cashflow_statements(symbol, limit, period))
    
    @requires_plan(FMPPlan.BASIC)
    async def aas_reported_financial_statements(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        '''
        Retrieve comprehensive financial statements as reported by companies. 
        Access complete data across income, balance sheet, and cash flow statements in their original form for detailed analysis.
        
        Args:
            period: e.g. annual
        '''
        endpoint = 'financial-statement-full-as-reported'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        if period:
            params['period'] = period
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def as_reported_financial_statements(self, symbol: str, limit: int | None = None, period: str | None = None) -> list[dict]:
        return asyncio.run(self.aas_reported_financial_statements(symbol, limit, period))
        