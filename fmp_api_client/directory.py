from typing import Literal

import asyncio

from fmp_api_client.base import Base


class Directory(Base):
    async def aavailable_exchanges(self) -> list[dict[Literal['exchange'], str]]:
        return await self._request('available-exchanges')
    
    def available_exchanges(self) -> list[dict[Literal['exchange'], str]]:
        return asyncio.run(self.aavailable_exchanges())