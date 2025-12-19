-- models/staging/stg_transactions.sql
SELECT
    transaction_id,
    price,
    living_area,
    rooms,
    latitude,
    longitude,
    transaction_date
FROM public.raw_real_estate_transactions
WHERE price IS NOT NULL
