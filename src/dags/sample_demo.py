from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

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
    'airflow-demo',
    default_args=default_args,
    description='A simple DAG for ETL process',
    schedule_interval='@daily',
)


# Define functions for ETL tasks
def extract_data():
    # Simulate extracting data from source
    print("Extracting data")


def transform_data():
    # Simulate transforming the extracted data
    print("Transforming data")


def load_data():
    # Simulate loading the transformed data to destination
    print("Loading data")


# Define the tasks
start_task = EmptyOperator(task_id='start', dag=dag)

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

end_task = EmptyOperator(task_id='end', dag=dag)

start_task >> extract_task >> transform_task >> load_task >> end_task
