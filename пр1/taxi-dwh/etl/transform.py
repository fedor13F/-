import pandas as pd


def build_dim_date(trips: pd.DataFrame) -> pd.DataFrame:
    """Уникальные даты из поездок + календарные атрибуты."""
    dt = pd.to_datetime(trips["started_at"]).dt.normalize()
    unique_dates = dt.drop_duplicates().sort_values().reset_index(drop=True)

    df = pd.DataFrame({"full_date": unique_dates})
    df["date_id"]      = df["full_date"].dt.strftime("%Y%m%d").astype("uint32")
    df["year"]         = df["full_date"].dt.year.astype("uint16")
    df["quarter"]      = df["full_date"].dt.quarter.astype("uint8")
    df["month"]        = df["full_date"].dt.month.astype("uint8")
    df["month_name"]   = df["full_date"].dt.strftime("%B")
    df["day"]          = df["full_date"].dt.day.astype("uint8")
    df["weekday"]      = (df["full_date"].dt.weekday + 1).astype("uint8")
    df["weekday_name"] = df["full_date"].dt.strftime("%A")

    return df[[
        "date_id", "full_date", "year", "quarter", "month",
        "month_name", "day", "weekday", "weekday_name"
    ]]


def build_dim_city(cities: pd.DataFrame, regions: pd.DataFrame) -> pd.DataFrame:
    """Город + регион денормализованно (звезда)."""
    df = cities.merge(regions, on="region_id", suffixes=("_city", "_region"))
    return pd.DataFrame({
        "city_id":     df["city_id"].astype("uint32"),
        "city_name":   df["name_city"],
        "region_name": df["name_region"],
    })


def build_dim_driver(drivers: pd.DataFrame, cities: pd.DataFrame) -> pd.DataFrame:
    """Водитель + город денормализованно."""
    df = drivers.merge(
        cities[["city_id", "name"]].rename(columns={"name": "city_name"}),
        on="city_id", how="left"
    )
    return pd.DataFrame({
        "driver_id":   df["driver_id"].astype("uint32"),
        "driver_name": df["name"],
        "rating":      df["rating"].astype("float32"),
        "city_name":   df["city_name"].fillna("Unknown"),
    })


def build_dim_car(cars: pd.DataFrame, drivers: pd.DataFrame) -> pd.DataFrame:
    """Машина + имя водителя денормализованно."""
    df = cars.merge(
        drivers[["driver_id", "name"]].rename(columns={"name": "driver_name"}),
        on="driver_id", how="left"
    )
    return pd.DataFrame({
        "car_id":      df["car_id"].astype("uint32"),
        "model":       df["model"],
        "class":       df["class"],
        "driver_name": df["driver_name"].fillna("Unknown"),
    })


def build_fact_trips(trips: pd.DataFrame) -> pd.DataFrame:
    """Факт-таблица: поездки + date_id + hour."""
    df = trips.copy()
    df["started_at"] = pd.to_datetime(df["started_at"])

    df["date_id"] = df["started_at"].dt.strftime("%Y%m%d").astype("uint32")
    df["hour"]    = df["started_at"].dt.hour.astype("uint8")

    return pd.DataFrame({
        "date_id":      df["date_id"],
        "hour":         df["hour"],
        "driver_id":    df["driver_id"].astype("uint32"),
        "car_id":       df["car_id"].astype("uint32"),
        "city_id":      df["city_id"].astype("uint32"),
        "duration_min": df["duration_min"].astype("uint32"),
        "distance_km":  df["distance_km"].astype("float64"),
        "price":        df["price"].astype("float64"),
        "status":       df["status"],
    })
