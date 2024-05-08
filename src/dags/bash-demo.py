from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG("sample_bash_dag_id",
         start_date=datetime(2024, 5, 7),
         schedule_interval=None,
         catchup=True
         ) as dag:
    bash_task_1 = BashOperator(
        task_id="task_id_1",
        bash_command='echo "This is a sample Task"',
    )
