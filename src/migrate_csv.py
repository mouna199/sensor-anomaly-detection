from transformers import sensor_transformer as st
from loaders import timescale_loader as tl
from extractors import csv_extractor as ce

FILE_PATH = "/home/mouna/Projects_data/sensordata_migration_prediction/data/raw/SKAB_data.csv"

DB_CONFIG = {'host': 'localhost',
            'port':'5432',
            'dbname':'migration_db',
            'user':'postgres',
            'password':'postgres'
            }

df = ce.load_csv_data(FILE_PATH)
df = st.transform_dataframe(df)
tl.load_to_timescale(df, DB_CONFIG)


