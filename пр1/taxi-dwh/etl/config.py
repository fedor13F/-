import os
from pathlib import Path
from dotenv import load_dotenv


env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

# PostgreSQL OLTP
PG = {
    "host": os.getenv("PG_HOST", "localhost"),
    "port": int(os.getenv("PG_PORT", 5433)),
    "db":   os.getenv("PG_DB", "taxi_oltp"),
    "user": os.getenv("PG_USER", "taxi"),
    "pass": os.getenv("PG_PASS", "taxi"),
}

# ClickHouse DWH
CH = {
    "host": os.getenv("CH_HOST", "localhost"),
    "port": int(os.getenv("CH_PORT", 8123)),
    "db":   os.getenv("CH_DB", "dwh"),
    "user": os.getenv("CH_USER", "dwh"),
    "pass": os.getenv("CH_PASS", "dwh"),
}
