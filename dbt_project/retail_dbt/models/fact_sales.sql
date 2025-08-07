{{ config(
    materialized='incremental',
    incremental_strategy='merge',
    unique_key='"InvoiceNo"',
) }}

SELECT
    "InvoiceNo",
    SUM("Quantity") AS total_items,
    SUM("TotalAmount") AS total_amount
FROM {{ ref('stg_sales') }}
{% if is_incremental() %}
    where "InvoiceNo" not in (select "InvoiceNo" from {{ this }})
{% else %}
    where "InvoiceNo" is not null
{% endif %}
GROUP BY "InvoiceNo"
