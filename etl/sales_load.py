from py_compile import main
import pandas as pd
from sqlalchemy import create_engine,text

def main():
    # Load raw data
    df = pd.read_csv("/opt/airflow/data/raw/sales.csv")  # absolute path in container

    # Clean and transform
    df = df.dropna(subset=["InvoiceNo", "Quantity", "UnitPrice"])
    df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

    # PostgreSQL connection string (inside docker network)
    engine = create_engine("postgresql://airflow:airflow@postgres:5432/analytics")

    with engine.begin() as conn:
        conn.execute(text("DROP TABLE IF EXISTS data_etl.sales_clean CASCADE"))
    # Load cleaned data to PostgreSQL
    df.to_sql("sales_clean", engine,schema="data_etl", if_exists="replace", index=False)

    print("✅ ETL Completed Successfully!")

if __name__ == "__main__":
    main()
