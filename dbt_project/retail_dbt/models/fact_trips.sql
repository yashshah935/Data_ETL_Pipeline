{{ config(
    materialized='table'
) }}

WITH cleaned AS (
    SELECT
        CAST("VendorID" AS INTEGER) AS vendor_id,
        CAST("passenger_count" AS INTEGER) AS passenger_count,
        CAST("trip_distance" AS FLOAT) AS trip_distance,
        CAST("RatecodeID" AS INTEGER) AS rate_code_id,
        CAST("store_and_fwd_flag" AS TEXT) AS store_and_fwd_flag,
        CAST("PULocationID" AS INTEGER) AS pickup_location_id,
        CAST("DOLocationID" AS INTEGER) AS dropoff_location_id,
        CAST("payment_type" AS INTEGER) AS payment_type,
        CAST("fare_amount" AS FLOAT) AS fare_amount,
        CAST("extra" AS FLOAT) AS extra,
        CAST("mta_tax" AS FLOAT) AS mta_tax,
        CAST("tip_amount" AS FLOAT) AS tip_amount,
        CAST("tolls_amount" AS FLOAT) AS tolls_amount,
        CAST("improvement_surcharge" AS FLOAT) AS improvement_surcharge,
        CAST("total_amount" AS FLOAT) AS total_amount,
        CAST("congestion_surcharge" AS FLOAT) AS congestion_surcharge,
        CAST("Airport_fee" AS FLOAT) AS airport_fee,
        CAST("cbd_congestion_fee" AS FLOAT) AS cbd_congestion_fee,
        "tpep_pickup_datetime" AS pickup_datetime,
        "tpep_dropoff_datetime" AS dropoff_datetime,

        -- Derived fields
        CAST(EXTRACT(EPOCH FROM ("tpep_dropoff_datetime" - "tpep_pickup_datetime")) / 60.0 AS DECIMAL(10,2) ) AS trip_duration_mins,
       CAST(
            CASE 
                WHEN EXTRACT(EPOCH FROM ("tpep_dropoff_datetime" - "tpep_pickup_datetime")) > 0 
                    AND "trip_distance" IS NOT NULL AND "trip_distance" > 0
                THEN "trip_distance" / (EXTRACT(EPOCH FROM ("tpep_dropoff_datetime" - "tpep_pickup_datetime")) / 3600.0)
                ELSE NULL 
            END AS DECIMAL(10, 2)
        ) AS avg_speed_mph

    FROM {{ source('data_etl', 'raw_taxi_data') }}
)

SELECT *
FROM cleaned
WHERE pickup_datetime IS NOT NULL
  AND dropoff_datetime IS NOT NULL
  AND trip_distance >= 0
  AND fare_amount >= 0
