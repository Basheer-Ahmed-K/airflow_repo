import json

from airflow import DAG
from airflow.providers.http.operators.http import HttpOperator
from datetime import datetime

with DAG(
        dag_id="HTTP-demo",
        start_date=datetime(2024, 5, 8),
        schedule_interval='@weekly',
        catchup=False
) as dag:
    demo_http = HttpOperator(
        task_id="get-http",
        http_conn_id="demo-conn",
        endpoint="api/users?page=2",
        response_filter=lambda response: json.loads(response.data)
    )
