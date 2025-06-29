from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess
from airflow.operators.bash import BashOperator

default_args = {
    'start_date': datetime(2024, 1, 1),
    'catchup': False
}

def run_etl():
    subprocess.run(["python3", "/opt/airflow/etl/sales_load.py"], check=True)

with DAG("retail_etl_local", schedule='@daily', default_args=default_args) as dag:
    etl_task = PythonOperator(
        task_id="load_data",
        python_callable=run_etl
    )

    run_dbt = BashOperator(
        task_id="dbt_transform",
        bash_command="docker exec dbt_container dbt run --project-dir /usr/app",
        dag=dag
    )
    etl_task >> run_dbt
