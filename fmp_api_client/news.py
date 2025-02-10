import asyncio
import datetime

from fmp_api_client.base import Base
from fmp_api_client.plan import FMPPlan, requires_plan


class News(Base):
    _base_endpoint = 'news'
    
    @requires_plan(FMPPlan.BASIC)
    async def aFMP_articles(
        self,
        page: int | None = None,
        limit: int | None = None,
        # NOTE: custom params
        start_date: str='',
        end_date: str='',
        symbols: list[str] | None = None,
    ) -> list[dict]:
        '''
        Access the latest articles from Financial Modeling Prep. 
        Get comprehensive updates including headlines, snippets, and publication URLs.
        '''
        endpoint = 'fmp-articles'
        params = {}
        start_date, end_date = self._prepare_dates(start_date, end_date)
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit
        if result := await self._request(endpoint, params=params):
            if symbols:
                symbols = [s.upper() for s in symbols]
            result = [
                r for r in result 
                if start_date <= datetime.datetime.strptime(r['date'], '%Y-%m-%d %H:%M:%S') <= end_date
                and (not symbols or r['tickers'].split(':')[-1] in symbols)
            ]
        return result
    
    @requires_plan(FMPPlan.BASIC)
    def FMP_articles(
        self,
        page: int | None = None,
        limit: int | None = None,
        # NOTE: custom params
        start_date: str='',
        end_date: str='',
        symbols: list[str] | None = None,
    ) -> list[dict]:
        return asyncio.run(
            self.aFMP_articles(
                page=page, 
                limit=limit, 
                start_date=start_date, 
                end_date=end_date,
                symbols=symbols,
            )
        )

    @requires_plan(FMPPlan.STARTER)
    async def ageneral_news(
        self, 
        from_: str = '',
        to: str = '',
        page: int | None = None,
        limit: int | None = None,
    ) -> list[dict]:
        '''
        Access the latest general news articles from a variety of sources. 
        Obtain headlines, snippets, and publication URLs for comprehensive news coverage.
        '''
        endpoint = f'{self._base_endpoint}/general-latest'
        params = {}
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit
        result = await self._request(endpoint, params=params)
        return result
    
    @requires_plan(FMPPlan.STARTER)
    def general_news(
        self,
        from_: str = '',
        to: str = '',
        page: int | None = None,
        limit: int | None = None,
    ) -> list[dict]:
        return asyncio.run(self.ageneral_news(from_, to, page, limit))
    
    @requires_plan(FMPPlan.PREMIUM)
    async def apress_releases(
        self,
        from_: str = '',
        to: str = '',
        page: int | None = None,
        limit: int | None = None,
        # NOTE: custom params
        symbols: list[str] | None = None,
    ) -> list[dict]:
        '''
        Access official company press releases. 
        Get real-time updates on corporate announcements, earnings reports, mergers, and more.
        '''
        endpoint = f'{self._base_endpoint}/press-releases-latest'
        params = {}
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit
        if result := await self._request(endpoint, params=params):
            if symbols:
                symbols = [s.upper() for s in symbols]
                result = [r for r in result if r['symbol'] in symbols]
        return result
    
    @requires_plan(FMPPlan.PREMIUM)
    def press_releases(
        self,
        from_: str = '',
        to: str = '',
        page: int | None = None,
        limit: int | None = None,
        # NOTE: custom params
        symbols: list[str] | None = None,
    ) -> list[dict]:
        return asyncio.run(self.apress_releases(from_, to, page, limit, symbols))
    
    @requires_plan(FMPPlan.STARTER)
    async def astock_news(
        self,
        from_: str = '',
        to: str = '',
        page: int | None = None,
        limit: int | None = None,
        # NOTE: custom params
        symbols: list[str] | None = None,
    ) -> list[dict]:
        '''
        Stay informed with the latest stock market news. 
        Access headlines, snippets, publication URLs, and ticker symbols for the most recent articles from a variety of sources.
        ''' 
        endpoint = f'{self._base_endpoint}/stock-latest'
        params = {}
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit
        if result := await self._request(endpoint, params=params):
            if symbols:
                symbols = [s.upper() for s in symbols]
                result = [r for r in result if r['symbol'] in symbols]
        return result
    
    @requires_plan(FMPPlan.STARTER)
    def stock_news(
        self,
        from_: str = '',
        to: str = '',
        page: int | None = None,
        limit: int | None = None,
        # NOTE: custom params
        symbols: list[str] | None = None,
    ) -> list[dict]:
        return asyncio.run(
            self.astock_news(
                from_=from_, 
                to=to, 
                page=page, 
                limit=limit, 
                symbols=symbols
            )
        )
    
    @requires_plan(FMPPlan.STARTER)
    async def acrypto_news(
        self,
        from_: str = '',
        to: str = '',
        page: int | None = None,
        limit: int | None = None,
        # NOTE: custom params
        symbols: list[str] | None = None,  # e.g. BTCUSD
    ) -> list[dict]:
        '''
        Stay informed with the latest cryptocurrency news. 
        Access a curated list of articles from various sources, including headlines, snippets, and publication URLs.
        '''
        endpoint = f'{self._base_endpoint}/crypto-latest'
        params = {}
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit
        if result := await self._request(endpoint, params=params):
            if symbols:
                symbols = [s.upper() for s in symbols]
                result = [r for r in result if r['symbol'] in symbols]
        return result
    
    @requires_plan(FMPPlan.STARTER)
    def crypto_news(
        self,
        from_: str = '',
        to: str = '',
        page: int | None = None,
        limit: int | None = None,
        # NOTE: custom params
        symbols: list[str] | None = None,  # e.g. BTCUSD
    ) -> list[dict]:
        return asyncio.run(
            self.acrypto_news(
                from_=from_, 
                to=to, 
                page=page, 
                limit=limit, 
                symbols=symbols
            )
        )
    
    @requires_plan(FMPPlan.STARTER)
    async def aforex_news(
        self,
        from_: str = '',
        to: str = '',
        page: int | None = None,
        limit: int | None = None,   
        # NOTE: custom params
        symbols: list[str] | None = None,  # e.g. GBPUSD
    ) -> list[dict]:
        '''
        Stay updated with the latest forex news articles from various sources. 
        Access headlines, snippets, and publication URLs for comprehensive market insights.
        '''
        endpoint = f'{self._base_endpoint}/forex-latest'
        params = {}
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit
        if result := await self._request(endpoint, params=params):
            if symbols:
                symbols = [s.upper() for s in symbols]
                result = [r for r in result if r['symbol'] in symbols]
        return result
    
    @requires_plan(FMPPlan.STARTER)
    def forex_news(
        self,
        from_: str = '',
        to: str = '',
        page: int | None = None,
        limit: int | None = None,
        # NOTE: custom params
        symbols: list[str] | None = None,  # e.g. GBPUSD
    ) -> list[dict]:
        return asyncio.run(
            self.aforex_news(
                from_=from_, 
                to=to, 
                page=page, 
                limit=limit, 
                symbols=symbols
            )
        )
    
    @requires_plan(FMPPlan.PREMIUM)
    async def asearch_press_releases(
        self,
        symbols: list[str],
        from_: str = '',
        to: str = '',
        page: int | None = None,
        limit: int | None = None,   
    ) -> list[dict]:
        endpoint = f'{self._base_endpoint}/press-releases'
        params = {'symbols': ','.join(symbols)}
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.PREMIUM)
    def search_press_releases(
        self,
        symbols: list[str],
        from_: str = '',
        to: str = '',
        page: int | None = None,
        limit: int | None = None,           
    ) -> list[dict]:
        return asyncio.run(
            self.asearch_press_releases(
                symbols,
                from_=from_,
                to=to,
                page=page,
                limit=limit,
            )
        )
    
    @requires_plan(FMPPlan.STARTER)
    async def asearch_stock_news(
        self,
        symbols: list[str],
        from_: str='',
        to: str='',
        page: int | None=None,
        limit: int | None=None,
    ) -> list[dict]:
        '''
        Search for stock-related news. 
        Find specific stock news by entering a ticker symbol or company name to track the latest developments.
        '''
        endpoint = f'{self._base_endpoint}/stock'
        params = {'symbols': ','.join(symbols)}
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.STARTER)
    def search_stock_news(
        self,
        symbols: list[str],
        from_: str='',
        to: str='',
        page: int | None=None,
        limit: int | None=None,
    ) -> list[dict]:
        return asyncio.run(
            self.asearch_stock_news(
                symbols,
                from_=from_,
                to=to,
                page=page,
                limit=limit,
            )
        )
        
    @requires_plan(FMPPlan.STARTER)
    async def asearch_crypto_news(
        self,
        symbols: list[str],
        from_: str='',
        to: str='',
        page: int | None=None,
        limit: int | None=None,
    ) -> list[dict]:
        '''
        Search for cryptocurrency news. 
        Retrieve news related to specific coins or tokens by entering their name or symbol.
        '''
        endpoint = f'{self._base_endpoint}/crypto'
        params = {'symbols': ','.join(symbols)}
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.STARTER)
    def search_crypto_news(
        self,
        symbols: list[str],
        from_: str='',
        to: str='',
        page: int | None=None,
        limit: int | None=None,
    ) -> list[dict]:
        return asyncio.run(
            self.asearch_crypto_news(
                symbols,
                from_=from_,
                to=to,
                page=page,
                limit=limit,
            )
        )
        
    @requires_plan(FMPPlan.STARTER)
    async def asearch_forex_news(
        self,
        symbols: list[str],
        from_: str='',
        to: str='',
        page: int | None=None,
        limit: int | None=None,
    ) -> list[dict]:
        '''
        Search for foreign exchange news. 
        Find targeted news on specific currency pairs by entering their symbols for focused updates.
        '''
        endpoint = f'{self._base_endpoint}/forex'
        params = {'symbols': ','.join(symbols)}
        if from_:
            params['from'] = from_
        if to:
            params['to'] = to
        if page:
            params['page'] = page
        if limit:
            params['limit'] = limit
        return await self._request(endpoint, params=params)
    
    @requires_plan(FMPPlan.STARTER)
    def search_forex_news(
        self,
        symbols: list[str],
        from_: str='',
        to: str='',
        page: int | None=None,
        limit: int | None=None,
    ) -> list[dict]:
        return asyncio.run(
            self.asearch_forex_news(
                symbols,
                from_=from_,
                to=to,
                page=page,
                limit=limit,
            )
        )
