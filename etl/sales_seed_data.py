import pandas as pd
import random


# Sample products
products = [
    ("85123A", "WHITE HANGER", 2.55),
    ("71053", "BLUE MUG", 3.39),
    ("84406B", "SET OF 3 CAKE TINS", 4.95),
    ("84029G", "RED PLATE", 1.25),
    ("21730", "GLASS VASE", 5.75),
    ("85099B", "WHITE CANDLE", 1.65),
    ("84879", "TEA TOWEL", 2.35),
    ("22720", "LED LAMP", 6.89),
    ("79321", "BAMBOO BOWL", 3.49),
    ("21931", "PINK NOTEBOOK", 1.99)
]

rows = []

for i in range(1000):
    invoice_no = 536365 + random.randint(0, 200)
    stock_code, description, unit_price = random.choice(products)
    quantity = random.randint(1, 12)
    rows.append([invoice_no, stock_code, description, quantity, unit_price])

df = pd.DataFrame(rows, columns=["InvoiceNo", "StockCode", "Description", "Quantity", "UnitPrice"])

# Save to CSV
df.to_csv("data/raw/sales.csv", index=False)
