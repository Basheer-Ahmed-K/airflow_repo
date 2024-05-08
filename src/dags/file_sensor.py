from airflow.sensors.filesystem import FileSensor
from airflow import DAG
from datetime import datetime

default_args = {
    'owner': 'noob',
    'retries': 1,
    'retries_delay': 3,
}
with DAG(
        default_args=default_args,
        dag_id="sensor_demo",
        start_date=datetime(2024, 5, 8),
        catchup=False,
        schedule_interval='@daily'  # @daily is called presets,
) as dag:
    wait_for_file = FileSensor(task_id="wait_for_file",
                               fs_conn_id='wait_for_file',
                               filepath='customer.py',
                               mode='reschedule',
                               poke_interval=30)
