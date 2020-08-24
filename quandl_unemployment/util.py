"""Utilities for fetching and organizing 
data from the Quandl api.
"""

from datetime import datetime
from quandl_unemployment.config import env


def get_today() -> str:
    """Get today's date as a string.
    returns -> str: today
    """
    return str(datetime.now().date())


def get_api_key() -> str:
    """Get api key from config.
    """
    return env['QUANDL_API_KEY']