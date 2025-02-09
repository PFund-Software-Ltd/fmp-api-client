from enum import IntEnum
from functools import wraps


class FMPPlan(IntEnum):
    BASIC = 0  # Free
    STARTER = 1
    PREMIUM = 2
    ULTIMATE = 3


def requires_plan(minimum_plan: FMPPlan):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper.required_plan = minimum_plan
        return wrapper
    return decorator