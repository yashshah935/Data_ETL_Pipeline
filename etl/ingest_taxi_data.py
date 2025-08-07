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

    print(f"📦 Initial partitions: {df.rdd.getNumPartitions()}")

    # Optional: Use repartition before transformations or large operations
    df = df.repartition(4)  # change number of partitions as needed
    print(f"🔄 After repartition(4): {df.rdd.getNumPartitions()}")

    # Cast datetime fields
    df = df.withColumn("tpep_pickup_datetime", col("tpep_pickup_datetime").cast("timestamp")) \
        .withColumn("tpep_dropoff_datetime", col("tpep_dropoff_datetime").cast("timestamp"))

    # Optional: Reduce partitions before writing to avoid too many small DB inserts
    df = df.coalesce(2)
    print(f"📉 After coalesce(2): {df.rdd.getNumPartitions()}")

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
        # ✅ Check if the table exists first
        result = conn.execute(text("""
            SELECT EXISTS (
                SELECT 1 FROM information_schema.tables 
                WHERE table_schema = 'data_etl' AND table_name = 'raw_taxi_data'
            )
        """))
        
        exists = result.scalar()
        
        if exists:
            print("🔄 Truncating existing table...")
            conn.execute(text("TRUNCATE TABLE data_etl.raw_taxi_data"))
        else:
            print("ℹ️ Table 'data_etl.raw_taxi_data' does not exist. Skipping truncate.")

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