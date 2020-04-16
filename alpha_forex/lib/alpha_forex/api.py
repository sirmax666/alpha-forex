# -----------------------------------------------------------------------------
# api
# -----------------------------------------------------------------------------
# Author: Maxime Sirois
# -----------------------------------------------------------------------------
"""
The API Class that is used to get quotes.
"""
# -----------------------------------------------------------------------------


import logging
import requests

logger = logging.getLogger(__name__)


class API:

    """Parent API class"""
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key

    def _get(self, payload):
        payload.update({'apikey': self.api_key})
        logger.debug(payload)
        return requests.get(self.url, params=payload)


class AlphaVantageClient(API):

    def get_fx_rate(self, from_currency, to_currency, reach='exchange'):
        function_map = {
            "exchange": "CURRENCY_EXCHANGE_RATE",
            "intraday": "FX_INTRADAY",
            "daily": "FX_DAILY",
            "weekly": "FX_WEEKLY",
            "monthly": "FX_MONTHLY"
        }
        try:
            function = function_map[reach]
        except KeyError:
            logger.error(f"The reach argument value does not exist: '{reach}'")
            raise

        payload = {
            "function": function,
            "from_currency": from_currency,
            "to_currency": to_currency
        }
        return self._get(payload)
