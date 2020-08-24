import requests
import json
import pandas as pd

from dbnomics.config import env

class API:

    def __init__(self, url):
        self.url = url
    
    #def build_url(self):
    #    url = 'https://api.db.nomics.world/v22/'
    #    url += 'series/Eurostat/sts_trtu_m/M.TOVT.G47.CA.PCH_SM.EA19'
    #    url += '?observations=1'
    #    self.url = url

    def __repr__(self) -> pd.DataFrame:
        return repr(self.df)

    def get_response(self):
        r = requests.get(self.url)
        self.r_json = r.json()

    def get_data(self):
        self.get_response()
        periods = self.r_json['series']['docs'][0]['period']
        values = self.r_json['series']['docs'][0]['value']
        self.df = pd.DataFrame(values,index=periods)

    def add_colnames(self):
        self.df.columns = [self.r_json['series']['docs'][0]['dataset_name']]
