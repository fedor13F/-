import pandas as pd
from sqlalchemy import create_engine
from config import PG


def get_pg_engine():
    """Создаёт подключение к PostgreSQL OLTP."""
    url = (
        f"postgresql+psycopg2://{PG['user']}:{PG['pass']}"
        f"@{PG['host']}:{PG['port']}/{PG['db']}"
    )
    return create_engine(url)


def extract_all() -> dict:
    """Читает все OLTP-таблицы в pandas DataFrame."""
    engine = get_pg_engine()

    tables = {
        "regions": "SELECT * FROM regions",
        "cities":  "SELECT * FROM cities",
        "drivers": "SELECT * FROM drivers",
        "cars":    "SELECT * FROM cars",
        "trips":   "SELECT * FROM trips",
    }

    data = {}
    for name, sql in tables.items():
        df = pd.read_sql(sql, engine)
        print(f"  extract {name}: {len(df)} rows")
        data[name] = df

    return data
