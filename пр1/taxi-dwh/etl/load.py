import clickhouse_connect
import pandas as pd
from config import CH


def get_ch_client():
    """Создаёт подключение к ClickHouse."""
    return clickhouse_connect.get_client(
        host=CH["host"],
        port=CH["port"],
        username=CH["user"],
        password=CH["pass"],
        database=CH["db"],
    )


def load_dataframe(client, table: str, df: pd.DataFrame):
    """Вставляет DataFrame в таблицу ClickHouse."""
    if df.empty:
        print(f"  load {table}: SKIP (empty)")
        return

    client.insert_df(table, df)
    print(f"  load {table}: {len(df)} rows")
