import pandas as pd
from sqlalchemy import create_engine, text
import os

# Path to the Parquet file
parquet_path = "/opt/airflow/data/raw/taxi_data.parquet"  # Adjust for inside container

# PostgreSQL connection string
engine = create_engine("postgresql://airflow:airflow@postgres:5432/analytics")

def load_parquet_to_postgres():
    print("📥 Reading Parquet file...")
    df = pd.read_parquet(parquet_path)

    print(f"✅ Parquet file loaded: {df.shape[0]} rows")

    # Connect and truncate the old table
    with engine.begin() as conn:
        print("🧹 Dropping existing table (if any)...")
        conn.execute(text("DROP TABLE IF EXISTS data_etl.raw_taxi_data CASCADE"))

    # Insert into Postgres
    print("📦 Inserting data into PostgreSQL...")
    df.to_sql("raw_taxi_data", engine, schema="data_etl", if_exists="replace", index=False)

    print("✅ Ingestion complete!")

if __name__ == "__main__":
    load_parquet_to_postgres()
