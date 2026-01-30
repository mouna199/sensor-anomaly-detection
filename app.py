"""app.py"""
import streamlit as st
import psycopg2
import polars as pl
from src.transformers import sensor_transformer as str
from src.loaders import timescale_loader as tl
from src.extractors import csv_extractor as ce

FILE_PATH = "/home/mouna/Projects_data/sensordata_migration_prediction/data/raw/SKAB_data.csv"
############## pour le déploiment, j'ignore ça pour l'instant##########################
DB_CONFIG = {'host': 'localhost',
            'port':'5432',
            'dbname':'migration_db',
            'user':'postgres',
            'password':'postgres'
            }
con = psycopg2.connect(**DB_CONFIG)
df = pl.read_database(
    query = "SELECT * FROM sensors",
    connection = con,
)
###########################################################################################

df = ce.load_csv_data(FILE_PATH)
df = str.transform_dataframe(df)
for col in df.select(pl.all().exclude(["datetime"])).columns:
    st.line_chart(df,x='datetime',y=col)
