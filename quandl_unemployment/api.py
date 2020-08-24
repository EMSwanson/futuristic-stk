"""Define quandl API.
"""

import os
import numpy as np
import pandas as pd
import quandl
from quandl_unemployment.util import get_today
from quandl_unemployment.config import env, col_names, series_ids

class API:

    def __init__(self, series_ids=series_ids, 
                 date_start='2015-01-01', date_end=get_today()) -> None:
        self.date_start = date_start
        self.date_end = date_end
        self.series_ids = series_ids

    def __repr__(self) -> pd.DataFrame:
        return repr(self.df)

    def get_data(self) -> None:
         self.df = quandl.get(self.series_ids,
                         trim_start=self.date_start, 
                         trim_end=self.date_end, 
                         collapse = 'monthly')

    def add_colnames(self) -> None:
        self.df.columns = col_names
