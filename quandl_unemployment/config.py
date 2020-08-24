"""Configuration for Quandl API calls.
"""

import io, os

series_ids: list = ["FRED/UNRATE", "FRED/LNS14000003", "FRED/LNS14000006", \
    "FRED/LNS14000009", "FRED/LNU04032183"]
col_names: list = ['Unemployment', 'Unemp_White', 'Unemp_Black', \
    'Unemp_Hispanic','Unemp_Asian']
env: dict = {
    "QUANDL_API_KEY": "",
    "DATA_FOLDER": "",
}
    

