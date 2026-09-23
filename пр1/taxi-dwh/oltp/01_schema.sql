-- Регионы
CREATE TABLE regions (
    region_id   SERIAL PRIMARY KEY,
    name        TEXT NOT NULL
);

-- Города
CREATE TABLE cities (
    city_id     SERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
    region_id   INT REFERENCES regions(region_id)
);

-- Водители
CREATE TABLE drivers (
    driver_id   SERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
    rating      NUMERIC(3,2),
    city_id     INT REFERENCES cities(city_id)
);

-- Машины
CREATE TABLE cars (
    car_id      SERIAL PRIMARY KEY,
    model       TEXT NOT NULL,
    class       TEXT NOT NULL,
    driver_id   INT REFERENCES drivers(driver_id)
);

-- Поездки
CREATE TABLE trips (
    trip_id       SERIAL PRIMARY KEY,
    driver_id     INT REFERENCES drivers(driver_id),
    car_id        INT REFERENCES cars(car_id),
    city_id       INT REFERENCES cities(city_id),
    started_at    TIMESTAMP NOT NULL,
    duration_min  INT NOT NULL,
    distance_km   NUMERIC(6,2) NOT NULL,
    price         NUMERIC(10,2) NOT NULL,
    status        TEXT NOT NULL
);

-- Индексы
CREATE INDEX idx_trips_started_at ON trips(started_at);
CREATE INDEX idx_trips_driver     ON trips(driver_id);
CREATE INDEX idx_trips_city       ON trips(city_id);
