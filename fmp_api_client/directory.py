from typing import Literal

from fmp_api_client.base import Base


class Directory(Base):
    def available_exchanges(self) -> list[dict[Literal['exchange'], str]]:
        return self._request('available-exchanges')