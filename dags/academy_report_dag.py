from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="academy_report_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@monthly",
    catchup=False
) as dag:

    run_pipeline = BashOperator(
        task_id="run_pipeline",
        bash_command="python src/main.py"
    )
