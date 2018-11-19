from datetime import timedelta

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator


# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)

}

dag = DAG(
    'workshop_macros',
    default_args=default_args,
    description='A simple macros DAG',
    schedule_interval=timedelta(days=1),
    template_searchpath='/usr/local/airflow/sql'
)

task = BashOperator(
    task_id='echo',
    bash_command='echo "ds: {{ ds }}, ts: {{ts}}" && \
        echo "ds_nodash: {{ds_nodash}}" && \
        echo "task_id: {{task.task_id}}"',
    dag=dag)

task2 = BashOperator(
    task_id='echo_from_template',
    bash_command='bash_script.sh',
    dag=dag
)
