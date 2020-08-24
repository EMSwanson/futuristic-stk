import quandl
from quandl_unemployment.config import env

quandl.ApiConfig.api_key = env['QUANDL_API_KEY']
