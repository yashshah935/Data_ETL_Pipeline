SELECT
    "InvoiceNo",
    SUM("Quantity") AS total_items,
    SUM("TotalAmount") AS total_amount
FROM {{ ref('stg_sales') }}
GROUP BY "InvoiceNo"
