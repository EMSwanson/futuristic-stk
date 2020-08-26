"""Configuration for Quandl API calls.
"""

import io, os

series_ids: list = ["FRED/UNRATE", "FRED/LNS14000003", "FRED/LNS14000006", 
    "FRED/LNS14000009", "FRED/LNU04032183", "FRED/HOUST", "FRED/LNS14200000", 
    "FRED/M1109BUSM293NNBR", "MULTPL/SP500_PE_RATIO_MONTH", "MULTPL/SP500_DIV_YIELD_MONTH",
]
col_names: list = ['Unemployment', 'Unemp_White', 'Unemp_Black', 
    'Unemp_Hispanic','Unemp_Asian', 'Housing_Starts', 'Unemp_Part_Time', 
    'Dow_Prices', 'S&P_PE', 'S&P_DIV',
]
env: dict = {
    "QUANDL_API_KEY": "iMm6-pAoxxUuod3xYxFA",
    "DATA_FOLDER": "",
}
    

