"""Load data from apis.
"""

import pandas as pd
from quandl_unemployment.api import API as QAPI
from dbnomics.api import API as DAPI
from dbnomics.config import urls as dbnomics_urls


def gather(filename="api_data.csv") -> pd.DataFrame():
    quandl_data = QAPI()
    quandl_data.get_data()
    quandl_data.add_colnames()
    quandl_df = quandl_data.df
    quandl_df.to_csv(filename, encoding='utf-8')
    return quandl_df
