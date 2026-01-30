import polars as pl 
from pathlib import Path

def load_csv_data(file_path:str) -> pl.DataFrame:
    """
    Extraire les données f'un fichier CSV qui contient les données de capteurs.
    """
    path = Path(file_path)
    if not path.exists(): 
        raise FileNotFoundError(f"Le fichier {file_path} n'existe pas.")
    df = pl.read_csv(file_path, separator=";",try_parse_dates=True)
    return df
#df = load_csv_data("/home/mouna/Projects_data/sensordata_migration_prediction/data/raw/SKAB_data.csv")
#print(df)
