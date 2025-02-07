'''
For some endpoints where the output rarely changes, we hard-code the output in const.py.
e.g. for endpoint "available-exchanges", it has been stored as AVAILABLE_EXCHANGES in const.py.

This script will compare these constants (hardcoded API outputs) with the actual API outputs

This should be run regularly (as a cronjob) to keep the constants up to date.
'''
from fmp_api_client import print_warning
from fmp_api_client.client import FMPClient
from fmp_api_client.const import AVAILABLE_EXCHANGES


ENDPOINTS_TO_SYNC_WITH_CONSTANTS = [
    (
        ('directory', 'available_exchanges'), # (FMPClient category attribute, function name)
        AVAILABLE_EXCHANGES  # Corresponding constant in const.py
    )
]


# EXTEND: clean up the output format
def clean_api_output(function_name: str, api_output):
    if function_name == 'available_exchanges':
        api_output = [exchange['exchange'] for exchange in api_output]
    return api_output


if __name__ == '__main__':
    client = FMPClient()

    for (category_name, function_name), constant in ENDPOINTS_TO_SYNC_WITH_CONSTANTS:
        category = getattr(client, category_name)  # e.g. client.search, client.directory
        function = getattr(category, function_name)
        api_output = function()
        api_output = clean_api_output(function_name, api_output)
        if api_output != constant:
            print_warning(f'{function_name} has changed')
            