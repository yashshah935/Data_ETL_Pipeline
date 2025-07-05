from email.mime import text
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import os


def load_data():
    # Initialize SparkSession
    spark = SparkSession.builder \
        .appName("TaxiDataIngestion") \
        .config("spark.jars.packages", "org.postgresql:postgresql:42.6.0") \
        .getOrCreate()

    # Set log level to WARN to avoid clutter
    spark.sparkContext.setLogLevel("WARN")

    # Load Parquet file from mounted volume
    parquet_path = "/opt/airflow/data/raw/taxi_data.parquet"
    df = spark.read.parquet(parquet_path)

    # Cast datetime fields
    df = df.withColumn("tpep_pickup_datetime", col("tpep_pickup_datetime").cast("timestamp")) \
        .withColumn("tpep_dropoff_datetime", col("tpep_dropoff_datetime").cast("timestamp"))

    # PostgreSQL config
    postgres_url = "jdbc:postgresql://postgres:5432/analytics"
    postgres_properties = {
        "user": "airflow",
        "password": "airflow",
        "driver": "org.postgresql.Driver"
    }
    # Connect to PostgreSQL
    from sqlalchemy import create_engine,text
    engine = create_engine("postgresql://airflow:airflow@postgres:5432/analytics")

    # Truncate the existing table if it exists
    print("🧹 Truncating existing table (if any)...")
    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE data_etl.raw_taxi_data"))
    # Write data in chunks to PostgreSQL
    print("🚀 Writing to PostgreSQL (data_etl.raw_taxi_data)...")
    df.write \
        .jdbc(url=postgres_url,
            table="data_etl.raw_taxi_data",
            mode="append",
            properties=postgres_properties)

    print("✅ PySpark Ingestion Completed Successfully!")

if __name__ == "__main__":
    load_data()