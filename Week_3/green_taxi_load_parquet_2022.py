import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    # url = ''
    # response = requests.get(url)

    months = list(i for i in range(1, 13))

    df_list = [pd.read_parquet("https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-{:02d}.parquet".format(month)) for month in months]
    data = pd.concat(df_list)

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
