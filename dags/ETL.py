import sys
from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from datetime import datetime

import sys
sys.path.append('/opt/airflow')
default_args = {
    'start_date': datetime(2024, 1, 1),
    'catchup': False
}

with DAG("etl_process",
         schedule='@daily',
         default_args=default_args,
         tags=["etl"],
         description="ETL DAG using TaskFlow API",
         ) as dag:

    @task
    def run_sales_etl():
        print("Starting ETL process for sales...")
        # Instead of subprocess, import and run the script function directly
        from etl.sales_load import main as sales_main  # Assuming sales_load.py has a `main()` function
        sales_main()
        print("Ingestion completed for sales data.")

    @task
    def run_taxi_etl():
        print("Starting ETL process for taxi data...")
        from etl.ingest_taxi_data import load_data as taxi_main  # Assuming ingest_taxi_data.py has a `main()` function
        taxi_main()
        print("Ingestion completed for taxi data.")

    sales_task = run_sales_etl()
    taxi_task = run_taxi_etl()

    dbt_task = BashOperator(
        task_id="dbt_transform",
        bash_command="docker exec dbt_container dbt run --project-dir /usr/app",
    )

    [sales_task, taxi_task] >> dbt_task
