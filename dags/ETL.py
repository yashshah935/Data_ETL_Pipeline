from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess
from airflow.operators.bash import BashOperator

default_args = {
    'start_date': datetime(2024, 1, 1),
    'catchup': False
}

def run_sales_etl():
    print("Starting ETL process...")
    subprocess.run(["python3", "/opt/airflow/etl/sales_load.py"], check=True)
    print("Ingestion completed for sales data.")

def run_taxi_etl():
    print("Starting Taxi Data ETL process...")
    subprocess.run(["python3", "/opt/airflow/etl/ingest_taxi_data.py"], check=True)
    print("Ingestion completed for taxi data.")

with DAG("etl_process", schedule='@daily', default_args=default_args) as dag:
    sales_load = PythonOperator(
        task_id="load_sales_data",
        python_callable=run_sales_etl
    )

    taxi_load = PythonOperator(
        task_id="load_taxi_data",
        python_callable=run_taxi_etl
    )

    run_dbt = BashOperator(
        task_id="dbt_transform",
        bash_command="docker exec dbt_container dbt run --project-dir /usr/app",
        dag=dag
    )
    [sales_load,taxi_load] >> run_dbt
