import psycopg2
import polars as pl


def create_connection(db_config:dict)-> psycopg2.connect:
    # Create connection
    con = psycopg2.connect(
                    host = db_config['host'],
                    port = db_config['port'],
                    dbname = db_config['dbname'],
                    user = db_config['user'],
                    password = db_config['password'],
                    )
    return con


def create_table(cur)-> None:
    # Créer la table si elle n'existe pas
    cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS sensors (
            datetime TIMESTAMP PRIMARY KEY,
            current float,
            temperature float,
            accelerometer_1rms float,
            accelerometer_2rms float,
            volume_flow_rate_rms float,
            voltage float,
            pressure float,
            thermocouple float
    )
    '''
    )

def insert_data(cur, df:pl.DataFrame):
    # Insérer les données
    insert_query = '''
        INSERT INTO sensors(datetime,current,temperature, voltage, accelerometer_1rms,
        accelerometer_2rms,volume_flow_rate_rms,pressure,thermocouple)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    for row in df.iter_rows():
        cur.execute(insert_query,row)
    return cur


def load_to_timescale(df, DB_CONFIG)-> None:
    con = create_connection(DB_CONFIG)
    cur = con.cursor()
    create_table(cur)
    cur = insert_data(cur,df)
    con.commit()
    con.close()

#df_test = pl.DataFrame({
#    "datetime": ["2020-01-01 00:00:00", "2020-01-01 00:00:01"],
#    "current": [1.0, 1.1],
#    "temperature": [25.0, 25.1],
#    "accelerometer1RMS": [0.1, 0.2],
#    "accelerometer2RMS": [0.1, 0.2],
#    "flow_volume": [10.0, 10.1],
#    "rateRMS": [5.0, 5.1],
#    "pressure": [1.0, 1.1],
#    "thermocouple": [30.0, 30.1]
#})


#DB_CONFIG = {'host': 'localhost',
#            'port':'5432',
#            'dbname':'migration_db',
#            'user':'postgres',
#            'password':'postgres'
#            }

#load_to_timescale(df_test, DB_CONFIG)