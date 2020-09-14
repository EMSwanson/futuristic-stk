"""Load data from apis.
"""
import os
import logging
import boto3
from botocore.exceptions import ClientError
import pandas as pd

from quandl_unemployment.api import API as QAPI
#from dbnomics.api import API as DAPI
#from dbnomics.config import urls as dbnomics_urls

from settings import BUCKET


def gather(filename="data/api_data.csv") -> pd.DataFrame():
    """Run apis, write csv, and PUT data to S3.

    Args:
        filename (str, optional): Filename to save. 
        Defaults to "data/api_data.csv"

    Returns:
        quandl_df: pd.DataFrame with data downloaded.
    """
    quandl_data = QAPI()
    quandl_data.get_data()
    quandl_data.add_colnames()
    quandl_df = quandl_data.df
    print(quandl_df.head())
    os.makedirs('data', exist_ok=True)
    quandl_df.to_csv(filename, encoding='utf-8')
    upload_file('data/api_data.csv', BUCKET)
    return quandl_df


def upload_file(file_name, bucket, object_name=None):
    """[summary]

    Args:
        filename ([type]): [description]
        bucket ([type]): [description]
        object_name ([type], optional): [description]. Defaults to None.

    Returns:
        bool: True or false whether upload succeeded.
    """

    if object_name is None:
        object_name = file_name

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def main():
    df = gather()


if __name__ == "__main__":
    main()