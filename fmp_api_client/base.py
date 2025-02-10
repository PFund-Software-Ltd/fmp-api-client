from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fmp_api_client.client import FMPClient
    from fmp_api_client.plan import FMPPlan
    
import inspect
import datetime


class Base:
    def __init__(self, client: FMPClient):
        self._client = client
        self._request = client._request
    
    def _get_required_plan(self) -> FMPPlan:
        caller_frame = inspect.stack()[1]
        caller_function_name = caller_frame.function
        # Get the required plan from the caller's decorated method
        required_plan = getattr(self.__class__, caller_function_name).required_plan
        return required_plan

    def _prepare_dates(self, start_date: str, end_date: str) -> tuple[datetime.datetime, datetime.datetime]:
        def parse_date(date_str: str) -> datetime.datetime:
            try:
                # Try datetime format first
                return datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                try:
                    # Try date-only format
                    return datetime.datetime.strptime(date_str, '%Y-%m-%d')
                except ValueError:
                    raise ValueError(f"Date must be in 'YYYY-MM-DD' or 'YYYY-MM-DD HH:MM:SS' format, got: {date_str}")

        start_date = parse_date(start_date) if start_date else datetime.datetime.min
        end_date = parse_date(end_date) if end_date else datetime.datetime.max
        return start_date, end_date
