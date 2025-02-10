import asyncio
import datetime

from fmp_api_client.base import Base
from fmp_api_client.plan import requires_plan, FMPPlan


class Analyst(Base):
    @requires_plan(FMPPlan.BASIC)
    async def afinancial_estimates(
        self,
        symbol: str,
        period: str='',  # TODO: find out supported periods
        page: int | None = None,
        limit: int | None = None,
    ) -> list[dict]:
        '''
        Retrieve analyst financial estimates for stock symbols. 
        Access projected figures like revenue, earnings per share (EPS), and other key financial metrics as forecasted by industry analysts to inform your investment decisions.
        Args:
            period: e.g. 'annual'
            page: e.g. 0 shows the most recent analyst estimates
        '''
        endpoint = 'analyst-estimates'
        params = {'symbol': symbol}
        if period:
            params['period'] = period
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def financial_estimates(
        self, 
        symbol: str, 
        period: str='', 
        page: int | None = None, 
        limit: int | None = None,
    ) -> list[dict]:
        return asyncio.run(
            self.afinancial_estimates(
                symbol=symbol, 
                period=period, 
                page=page, 
                limit=limit
            )
        )

    @requires_plan(FMPPlan.BASIC)
    async def aratings_snapshot(
        self,
        symbol: str,
        limit: int | None = None,
    ) -> list[dict]:
        '''
        Quickly assess the financial health and performance of companies. 
        This provides a comprehensive snapshot of financial ratings for stock symbols in our database, based on various key financial ratios.
        '''
        endpoint = 'ratings-snapshot'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def ratings_snapshot(self, symbol: str, limit: int | None = None) -> list[dict]:
        return asyncio.run(
            self.aratings_snapshot(
                symbol=symbol, 
                limit=limit
            )
        )

    @requires_plan(FMPPlan.BASIC)
    async def ahistorical_ratings(
        self,
        symbol: str,
        limit: int | None=None,
    ) -> list[dict]:
        '''
        Track changes in financial performance over time. 
        This provides access to historical financial ratings for stock symbols in our database, allowing users to view ratings and key financial metric scores for specific dates.
        '''
        endpoint = 'ratings-historical'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def historical_ratings(self, symbol: str, limit: int | None = None) -> list[dict]:
        return asyncio.run(
            self.ahistorical_ratings(
                symbol=symbol, 
                limit=limit
            )
        )

    @requires_plan(FMPPlan.BASIC)
    async def aprice_target_summary(
        self,
        symbol: str,
        limit: int | None = None,
        page: int | None = None,
    ) -> list[dict]:
        '''
        Gain insights into analysts' expectations for stock prices. 
        This provides access to average price targets from analysts across various timeframes, helping investors assess future stock performance based on expert opinions.
        '''
        endpoint = 'price-target-summary'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        if page:
            params['page'] = page
        return await self._request(endpoint, params=params)

    @requires_plan(FMPPlan.BASIC)
    def price_target_summary(self, symbol: str, limit: int | None = None, page: str='') -> list[dict]:
        return asyncio.run(
            self.aprice_target_summary(
                symbol=symbol, 
                limit=limit, 
                page=page
            )
        )
    
    @requires_plan(FMPPlan.BASIC)
    async def aprice_target_consensus(
        self,
        symbol: str,
        limit: int | None = None,
        page: int | None = None,
    ) -> list[dict]:
        '''
        Access analysts' consensus price targets. 
        This provides high, low, median, and consensus price targets for stocks, offering investors a comprehensive view of market expectations for future stock prices.
        '''
        endpoint = 'price-target-consensus'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        if page:
            params['page'] = page
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def price_target_consensus(self, symbol: str, limit: int | None = None, page: int | None = None) -> list[dict]:
        return asyncio.run(
            self.aprice_target_consensus(
                symbol=symbol, 
                limit=limit, 
                page=page
            )
        )
    
    @requires_plan(FMPPlan.BASIC)
    async def aprice_target_news(
        self,
        symbol: str,
        limit: int | None = None,
        page: int | None = None,
    ) -> list[dict]:
        '''
        Stay informed with real-time updates on analysts' price targets for stocks. 
        Access the latest forecasts, stock prices at the time of the update, and direct links to trusted news sources for deeper insights.
        '''
        endpoint = 'price-target-news'
        params = {'symbol': symbol}
        if limit:
            params['limit'] = limit
        if page:
            params['page'] = page
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.BASIC)
    def price_target_news(
        self, 
        symbol: str, 
        limit: int | None = None, 
        page: int | None = None,
    ) -> list[dict]:
        return asyncio.run(
            self.aprice_target_news(
                symbol=symbol, 
                limit=limit, 
                page=page
            )
        )
    
    @requires_plan(FMPPlan.BASIC)
    async def aprice_target_latest_news(
        self,
        limit: int | None = None,
        page: int | None = None,
        # NOTE: custom params
        symbols: list[str] | None = None,
    ) -> list[dict]:
        '''
        Stay updated with the most recent analyst price target updates for ALL stock symbols. 
        Get access to detailed forecasts, stock prices at the time of the update, analyst insights, and direct links to news sources for deeper analysis.
        '''
        endpoint = 'price-target-latest-news'
        params = {}
        if limit:
            params['limit'] = limit
        if page:
            params['page'] = page
        if result := await self._request(endpoint, params=params):
            if symbols:
                symbols = [s.upper() for s in symbols]
                result = [r for r in result if r['symbol'] in symbols]
        return result
    
    @requires_plan(FMPPlan.BASIC)
    def price_target_latest_news(
        self,
        limit: int | None = None,
        page: int | None = None,
        # NOTE: custom params
        symbols: list[str] | None = None,
    ) -> list[dict]:
        return asyncio.run(
            self.aprice_target_latest_news(
                limit=limit, 
                page=page, 
                symbols=symbols,
            )
        )
    
    @requires_plan(FMPPlan.BASIC)
    async def astock_grades(
        self, 
        symbol: str,
        # NOTE: custom params
        start_date: str='',
        end_date: str='',
    ) -> list[dict]:
        '''
        Access the latest stock grades from top analysts and financial institutions. 
        Track grading actions, such as upgrades, downgrades, or maintained ratings, for specific stock symbols, providing valuable insight into how experts evaluate companies over time.
        Args:
            start_date: e.g. '2024-01-01'
            end_date: e.g. '2024-01-02'
        '''
        endpoint = 'grades'
        params = {'symbol': symbol}
        start_date, end_date = self._prepare_dates(start_date, end_date)
        if result := await self._request(endpoint, params=params):
            result = [
                r for r in result 
                if start_date <= datetime.datetime.strptime(r['date'], '%Y-%m-%d') <= end_date
            ]
        return result
    
    @requires_plan(FMPPlan.BASIC)
    def stock_grades(
        self, 
        symbol: str,
        # NOTE: custom params
        start_date: str='',
        end_date: str='',
    ) -> list[dict]:
        return asyncio.run(
            self.astock_grades(
                symbol=symbol, 
                start_date=start_date, 
                end_date=end_date
            )
        )
    
    @requires_plan(FMPPlan.BASIC)
    async def ahistorical_stock_grades(
        self,
        symbol: str,
        limit: int | None = None,
        # NOTE: custom params
        start_date: str='',
        end_date: str='',
    ) -> list[dict]:
        '''
        Access a comprehensive record of analyst grades. 
        This allows you to track historical changes in analyst ratings for specific stock symbol
        '''
        endpoint = 'grades-historical'
        params = {'symbol': symbol}
        start_date, end_date = self._prepare_dates(start_date, end_date)
        if limit:
            params['limit'] = limit
        if result := await self._request(endpoint, params=params):
            result = [
                r for r in result 
                if start_date <= datetime.datetime.strptime(r['date'], '%Y-%m-%d') <= end_date
            ]
        return result
    
    @requires_plan(FMPPlan.BASIC)
    def historical_stock_grades(
        self,
        symbol: str, 
        limit: int | None = None,
        # NOTE: custom params
        start_date: str='',
        end_date: str='',
    ) -> list[dict]:
        return asyncio.run(
            self.ahistorical_stock_grades(
                symbol=symbol, 
                limit=limit, 
                start_date=start_date, 
                end_date=end_date
            )
        )
    
    @requires_plan(FMPPlan.BASIC)
    async def astock_grades_summary(
        self,
        symbol: str,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[dict]:
        '''
        Quickly access an overall view of analyst ratings. 
        This provides a consolidated summary of market sentiment for individual stock symbols, including the total number of strong buy, buy, hold, sell, and strong sell ratings. 
        Understand the overall consensus on a stock’s outlook with just a few data points.
        '''
        endpoint = 'grades-consensus'
        params = {'symbol': symbol}
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)

    @requires_plan(FMPPlan.BASIC)
    def stock_grades_summary(
        self,
        symbol: str,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[dict]:
        return asyncio.run(
            self.astock_grades_summary(
                symbol=symbol, 
                page=page, 
                limit=limit
            )
        )
    
    @requires_plan(FMPPlan.BASIC)
    async def astock_grade_news(
        self,
        symbol: str,
        limit: int | None = None,
        page: int | None = None,
        # NOTE: custom params
        start_date: str='',
        end_date: str='',
    ) -> list[dict]:
        '''
        Stay informed on the latest analyst grade changes. 
        This provides real-time updates on stock rating changes, including the grading company, previous and new grades, and the action taken. 
        Direct links to trusted news sources and stock prices at the time of the update help you stay ahead of market trends and analyst opinions for specific stock symbols.
        '''
        endpoint = 'grades-news'
        params = {'symbol': symbol}
        start_date, end_date = self._prepare_dates(start_date, end_date)
        if limit:
            params['limit'] = limit
        if page:
            params['page'] = page
        if result := await self._request(endpoint, params=params):
            result = [
                r for r in result 
                if start_date <= datetime.datetime.strptime(r['publishedDate'], '%Y-%m-%dT%H:%M:%S.%fZ') <= end_date
            ]
        return result
    
    @requires_plan(FMPPlan.BASIC)
    def stock_grade_news(
        self,
        symbol: str,
        limit: int | None = None,
        page: int | None = None,
        # NOTE: custom params
        start_date: str='',
        end_date: str='',
    ) -> list[dict]:
        return asyncio.run(
            self.astock_grade_news(
                symbol=symbol, 
                limit=limit, 
                page=page, 
                start_date=start_date, 
                end_date=end_date
            )
        )
    
    @requires_plan(FMPPlan.BASIC)
    async def astock_grade_latest_news(
        self,
        limit: int | None = None,
        page: int | None = None,
        # NOTE: custom params
        symbols: list[str] | None = None,
        start_date: str='',
        end_date: str='',
    ) -> list[dict]:
        '''
        Stay informed on the latest stock rating changes. 
        This provides the most recent updates on analyst ratings for all stock symbols, including links to the original news sources. 
        Track stock price movements, grading firm actions, and market sentiment shifts in real time, sourced from trusted publishers.
        '''
        endpoint = 'grades-latest-news'
        params = {}
        start_date, end_date = self._prepare_dates(start_date, end_date)
        if limit:
            params['limit'] = limit
        if page:
            params['page'] = page
        if result := await self._request(endpoint, params=params):
            if symbols:
                symbols = [s.upper() for s in symbols]
            result = [
                r for r in result 
                if start_date <= datetime.datetime.strptime(r['publishedDate'], '%Y-%m-%dT%H:%M:%S.%fZ') <= end_date
                and (not symbols or r['symbol'] in symbols)
            ]
        return result
    
    @requires_plan(FMPPlan.BASIC)
    def stock_grade_latest_news(
        self,
        limit: int | None = None,
        page: int | None = None,
        # NOTE: custom params
        symbols: list[str] | None = None,
        start_date: str='',
        end_date: str='',
    ) -> list[dict]:
        return asyncio.run(
            self.astock_grade_latest_news(
                limit=limit, 
                page=page, 
                symbols=symbols, 
                start_date=start_date, 
                end_date=end_date
            )
        )
