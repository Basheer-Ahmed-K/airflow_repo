from random import randint
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from random import randint


def choose_best_model(ti):
    accuracies = ti.xcom_pull(task_ids=["first_model_training", "second_model_training", "third_model_training"])
    best_accuracy = max(accuracies)
    if best_accuracy > 8:
        return "accurate"
    return "inaccurate"


def model1():
    return randint(1, 10)


with DAG(
        dag_id="ML_workflow",
        start_date=datetime(2024, 5, 7),
        schedule_interval="@weekly",
        catchup=False
) as dag:
    first_training_model = PythonOperator(
        task_id="first_model_training",
        python_callable=model1
    )

    second_training_model = PythonOperator(
        task_id="second_model_training",
        python_callable=model1
    )

    third_training_model = PythonOperator(
        task_id="third_model_training",
        python_callable=model1
    )
    choose_best = PythonOperator(
        task_id="choose_best_model",
        python_callable=choose_best_model
    )
    accurate_model = BashOperator(
        task_id="accurate",
        bash_command="echo accurate"
    )
    inaccurate_model = BashOperator(
        task_id="inaccurate",
        bash_command="echo inaccurate"
    )
    [first_training_model, second_training_model, third_training_model] >> choose_best >> [accurate_model, inaccurate_model]