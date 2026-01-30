"""app.py"""
import streamlit as st
import psycopg2
import polars as pl


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
for col in df.select(pl.all().exclude(["datetime"])).columns:
    st.line_chart(df,x='datetime',y=col)
