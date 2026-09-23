CREATE DATABASE IF NOT EXISTS dwh;

-- Измерение: дата
CREATE TABLE IF NOT EXISTS dwh.dim_date (
    date_id       UInt32,
    full_date     Date,
    year          UInt16,
    quarter       UInt8,
    month         UInt8,
    month_name    String,
    day           UInt8,
    weekday       UInt8,
    weekday_name  String
) ENGINE = MergeTree()
ORDER BY date_id;

-- Измерение: город (звезда — регион внутри)
CREATE TABLE IF NOT EXISTS dwh.dim_city (
    city_id      UInt32,
    city_name    String,
    region_name  String
) ENGINE = MergeTree()
ORDER BY city_id;

-- Измерение: водитель
CREATE TABLE IF NOT EXISTS dwh.dim_driver (
    driver_id    UInt32,
    driver_name  String,
    rating       Decimal(3,2),
    city_name    String
) ENGINE = MergeTree()
ORDER BY driver_id;

-- Измерение: машина
CREATE TABLE IF NOT EXISTS dwh.dim_car (
    car_id       UInt32,
    model        String,
    class        String,
    driver_name  String
) ENGINE = MergeTree()
ORDER BY car_id;

-- Факт: поездки
CREATE TABLE IF NOT EXISTS dwh.fact_trips (
    date_id       UInt32,
    hour          UInt8,
    driver_id     UInt32,
    car_id        UInt32,
    city_id       UInt32,
    duration_min  UInt32,
    distance_km   Decimal(6,2),
    price         Decimal(10,2),
    status        String
) ENGINE = MergeTree()
PARTITION BY intDiv(date_id, 10000)
ORDER BY (date_id, hour, city_id, driver_id, car_id);
