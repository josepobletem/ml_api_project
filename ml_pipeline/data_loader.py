import pandas as pd
import psycopg2

def load_data_from_db(conn_str: str, query: str) -> pd.DataFrame:
    """Carga datos desde una base de datos PostgreSQL."""
    conn = psycopg2.connect(conn_str)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def load_data_from_csv(file_path: str) -> pd.DataFrame:
    """Carga datos desde un archivo CSV."""
    return pd.read_csv(file_path)
