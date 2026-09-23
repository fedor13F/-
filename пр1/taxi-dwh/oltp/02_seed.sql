-- Регионы: 5 штук
INSERT INTO regions (name) VALUES
  ('Сибирь'), ('Урал'), ('Центр'), ('Юг'), ('Дальний Восток');

-- Города: 20 штук, по 4 на регион
INSERT INTO cities (name, region_id)
SELECT 'Город-' || g, ((g - 1) / 4) + 1
FROM generate_series(1, 20) g;

-- Водители: 200 штук
INSERT INTO drivers (name, rating, city_id)
SELECT
  'Водитель-' || g,
  round((3.5 + random() * 1.5)::numeric, 2),
  ((g - 1) % 20) + 1
FROM generate_series(1, 200) g;

-- Машины: 200 штук
INSERT INTO cars (model, class, driver_id)
SELECT
  (ARRAY[
    'Kia Rio',
    'Hyundai Solaris',
    'Toyota Camry',
    'Skoda Octavia',
    'BMW 5',
    'Mercedes E'
  ])[(random() * 5 + 1)::int],
  (ARRAY['economy','comfort','business'])[(random() * 2 + 1)::int],
  g
FROM generate_series(1, 200) g;

-- Поездки: 50 000 за 2 года (2023–2024)
INSERT INTO trips (driver_id, car_id, city_id, started_at,
                   duration_min, distance_km, price, status)
SELECT
  d.driver_id,
  d.driver_id,
  d.city_id,
  TIMESTAMP '2023-01-01'
    + (random() * INTERVAL '730 days')
    + (random() * INTERVAL '24 hours'),
  (random() * 60 + 5)::int,
  round((random() * 30 + 1)::numeric, 2),
  round((random() * 1500 + 150)::numeric, 2),
  CASE WHEN random() < 0.9 THEN 'completed' ELSE 'cancelled' END
FROM generate_series(1, 50000) g
JOIN drivers d ON d.driver_id = ((g - 1) % 200) + 1;
