from airflow import DAG
from airflow.sensors.time_sensor import TimeSensor
from datetime import datetime, timedelta, time

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate the DAG
dag = DAG(
    'time-sensor',
    default_args=default_args,
    description='A simple DAG for ETL process',
    schedule_interval='@daily',
)

time_sensor = TimeSensor(
    task_id="wait_for_specific_task",
    target_time=time(9,0,0),
    dag=dag
)

