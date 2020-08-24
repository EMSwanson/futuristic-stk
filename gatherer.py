from quandl_unemployment.api import API as QAPI
from dbnomics.api import API as DAPI
from dbnomics.config import urls as dbnomics_urls

### Most of these apis will need to be defined as a class, then called as an instance of the same API, but with different calls repeatedly.

### quandl is pretty nice, and we might be able to get all the data in one call, im not sure.

### The other apis we will have to loop over.

quandl_data = QAPI()
quandl_data.get_data()
quandl_data.add_colnames()
quandl_df = quandl_data.df
print(quandl_df)

for url in dbnomics_urls:
    dbnomics_data = DAPI(url)
    dbnomics_data.get_data()
    dbnomics_data.add_colnames()
    dbnomics_df = dbnomics_data.df
    print(dbnomics_df)