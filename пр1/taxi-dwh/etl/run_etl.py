from extract import extract_all
from transform import (
    build_dim_date, build_dim_city, build_dim_driver,
    build_dim_car, build_fact_trips
)
from load import get_ch_client, load_dataframe


def main():
    print("=" * 50)
    print("TRUNCATE ClickHouse (очистка перед загрузкой)")
    print("=" * 50)
    client = get_ch_client()
    for table in ["fact_trips", "dim_date", "dim_city", "dim_driver", "dim_car"]:
        client.command(f"TRUNCATE TABLE dwh.{table}")
        print(f"  truncated dwh.{table}")
    
    print()
    print("=" * 50)
    print("EXTRACT (PostgreSQL → pandas)")
    print("=" * 50)
    raw = extract_all()

    print()
    print("=" * 50)
    print("TRANSFORM (OLTP → star schema)")
    print("=" * 50)
    dim_date   = build_dim_date(raw["trips"])
    dim_city   = build_dim_city(raw["cities"], raw["regions"])
    dim_driver = build_dim_driver(raw["drivers"], raw["cities"])
    dim_car    = build_dim_car(raw["cars"], raw["drivers"])
    fact_trips = build_fact_trips(raw["trips"])

    print(f"  dim_date:     {len(dim_date)} rows")
    print(f"  dim_city:     {len(dim_city)} rows")
    print(f"  dim_driver:   {len(dim_driver)} rows")
    print(f"  dim_car:      {len(dim_car)} rows")
    print(f"  fact_trips:   {len(fact_trips)} rows")

    print()
    print("=" * 50)
    print("LOAD (pandas → ClickHouse)")
    print("=" * 50)
    load_dataframe(client, "dwh.dim_date",   dim_date)
    load_dataframe(client, "dwh.dim_city",   dim_city)
    load_dataframe(client, "dwh.dim_driver", dim_driver)
    load_dataframe(client, "dwh.dim_car",    dim_car)
    load_dataframe(client, "dwh.fact_trips", fact_trips)

    print()
    print("Done.")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
