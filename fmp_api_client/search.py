from fmp_api_client.base import Base
from fmp_api_client.client import sync_async_handler


class Search(Base):
    '''
    # TODO: describe what this class does
    
    Prompt:
        ...
    
    '''
    
    def _stock_symbol_search(
        self, 
        query: str,
        limit: int | None = None,
        exchange: str = '',
    ) -> list[dict]:
        '''
        Search ticker symbol of any stock by company name or symbol across multiple global markets.
        
        # TODO: finish prompt
        Prompt:
            exchange should be provided for an exact match.
            Available exchanges:
                {AVAILABLE_EXCHANGES}
            
        Args:
            query: company name or symbol (e.g. AAPL)
            limit: number of results to return
            exchange: exchange name (e.g. NASDAQ)
            
        Returns:
            TODO
        '''
        params = {'query': query}
        if limit:
            params['limit'] = limit
        if exchange:
            params['exchange'] = exchange
        return self._request('search-symbol', params=params)
    astock_symbol_search, stock_symbol_search = sync_async_handler(_stock_symbol_search)