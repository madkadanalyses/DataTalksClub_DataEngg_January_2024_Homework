#!/usr/bin/env python
# coding: utf-8
import os
import argparse
import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse

def main(params):
    user = params.user
    password = params.password
    port = params.port
    host = params.host
    db = params.db
    url = params.url
    table_name = params.table_name

    if url.endswith('.csv.gz'):
        csv_name = 'output.csv.gz'
    else:
        csv_name = 'output.csv'

    #download the csv
    os.system(f'wget {url} -O {csv_name}')

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df = pd.read_csv(csv_name, iterator=True, chunksize=10)
    df_chunk = next(df)
    #df_chunk["lpep_pickup_datetime"] = pd.to_datetime(df_chunk["lpep_pickup_datetime"])
    #df_chunk["lpep_dropoff_datetime"] = pd.to_datetime(df_chunk["lpep_dropoff_datetime"])
    df_chunk.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
    df_chunk.to_sql(name=table_name, con=engine, if_exists='append')




    while True:

        try:
            time_start = time()
            df_chunk = next(df)
            
            #df_chunk["lpep_pickup_datetime"] = pd.to_datetime(df_chunk["lpep_pickup_datetime"])
            #df_chunk["lpep_dropoff_datetime"] = pd.to_datetime(df_chunk["lpep_dropoff_datetime"])

            df_chunk.to_sql(name=table_name, con=engine, if_exists='append')
            time_end = time()
            print("another chunk appended..., took %.3f seconds" % (time_end - time_start))
        except StopIteration:
            print("Finished injecting data into Postgres db as {} table".format(table_name))
            break



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Injest CSV into Postgres')
    parser.add_argument('--user',required=True, help='user name for Postgres')
    parser.add_argument('--password',required=True, help='pasword for Postgres')
    parser.add_argument('--port',required=True, help='port for Postgres')
    parser.add_argument('--host',required=True, help='host for Postgres')
    parser.add_argument('--db',required=True, help='database name for Postgres')
    parser.add_argument('--table_name',required=True, help='table name for Postgres')
    parser.add_argument('--url',required=True, help='url for data')
    args = parser.parse_args()
    main(args)

