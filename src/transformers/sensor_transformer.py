import polars as pl 
import logging

logger = logging.getLogger(__name__)

def drop_unused_columns(df:pl.DataFrame,columns:list[str]) -> pl.DataFrame:
    df = df.drop(columns)
    return df 


def pivot_sensors(df:pl.DataFrame) -> pl.DataFrame:
    df = df.pivot(on='id',index='datetime',values= 'value')
    return df 


def check_and_fill_nulls(df:pl.DataFrame) -> pl.DataFrame:
    null_count = df.null_count().row(0)
    total_nulls = sum(null_count)
    if total_nulls > 0:
        logger.info(f"Interpolation de {total_nulls} valeurs nulles") 
    return df.interpolate()


def check_and_drop_duplicates(df:pl.DataFrame) -> pl.DataFrame:
    initial = len(df)
    df = df.unique(subset = ['datetime'],keep="first", maintain_order=True)
    removed = initial - len(df)
    if removed > 0:
        logger.info(f"Suppression de {removed} doublons") 
    return df 


def convert_types(df:pl.DataFrame) -> pl.DataFrame:
    return df.with_columns([
        pl.col('datetime').str.to_datetime(), 
        pl.col('Current', 'Temperature', 'Accelerometer1RMS', 
               'Accelerometer2RMS', 'Flow', 'Volume', 
               'RateRMS', 'Pressure', 'Thermocouple').cast(pl.Float64)
    ])


def sort_dataframe(df:pl.DataFrame) -> pl.DataFrame:
    return df.sort('datetime')


def transform_dataframe(df:pl.DataFrame) -> pl.DataFrame:
    "Appliquer du traitement sur le dataframe des données extraites depuis csv"
    logger.info(f"Début transformation: {len(df)} lignes")
    df = (
        df
        .pipe(drop_unused_columns,['index'])
        .pipe(pivot_sensors)
        .pipe(convert_types)
        .pipe(sort_dataframe)
        .pipe(check_and_fill_nulls)
        .pipe(check_and_drop_duplicates)
          )
    logger.info(f"Fin transformation: {len(df)} lignes")
    return df
