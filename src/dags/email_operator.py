from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'noob',
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
    'email': ['basheer1801@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True
}

with DAG(
        dag_id="email-dag",
        start_date=datetime(2024, 5, 7),
        schedule_interval='@daily',
        default_args=default_args,
        catchup=False
) as dag:
    dummy_task = BashOperator(
        task_id="cd-cmd",
        bash_command="cd abcd"
    )

    # send_email = EmailOperator(
    #     task_id='send_email',
    #     to='ba184279@gmail.com',
    #     subject='Airflow Alert',
    #     html_content='<h1>Hi Coder,</h1><p>Your Airflow job has finished.</p>'
    # )
# send_email = EmailOperator(
#     task_id='send_email',
#     to='{{ task_instance.xcom_pull(task_ids='recipient_task') }}',
#     subject='{{ ds }}: Airflow Alert',
#     html_content='<p>{{ task_instance.xcom_pull(task_ids='message_task') }}</p>'
# )
