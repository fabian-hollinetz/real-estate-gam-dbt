-- models/features/gam_features.sql
SELECT
    price,
    living_area,
    rooms,
    EXTRACT(year FROM transaction_date) AS year,
    latitude,
    longitude
FROM {{ ref('fct_prices') }}
