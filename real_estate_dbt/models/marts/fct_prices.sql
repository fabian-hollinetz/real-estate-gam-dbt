-- models/marts/fct_prices.sql
SELECT
    transaction_date,
    living_area,
    rooms,
    price,
    latitude,
    longitude
FROM {{ ref('stg_transactions') }}
