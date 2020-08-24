"""Utilities for fetching and organizing 
data from the db_nomics api.
"""

from datetime import datetime
from dbnomics.config import env


def get_api_key() -> str:
    """Get api key from config.
    """
    return env['QUANDL_API_KEY']