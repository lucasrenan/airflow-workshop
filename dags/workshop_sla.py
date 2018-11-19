from datetime import timedelta

import airflow
from airflow import DAG
from airflow.operators.email_operator import EmailOperator
from airflow.operators.bash_operator import BashOperator


EMAIL = 'gerard.toonstra@localhost'

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': True,
    'start_date': airflow.utils.dates.days_ago(2),
    'email': [EMAIL],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
    'sla': timedelta(seconds=30),
    'execution_timeout': timedelta(minutes=1)
}

dag = DAG(
    'workshop_sla',
    default_args=default_args,
    description='A simple SLA demonstration DAG',
    schedule_interval=timedelta(days=1)
)

t1 = BashOperator(
    task_id='sleep_too_long',
    bash_command='sleep 50',
    dag=dag
)

email = EmailOperator(
    to=[EMAIL],
    subject='<type your personal message here>',
    html_content='<h1>hi</h1>',
    task_id='email_results',
    dag=dag
)

t2 = BashOperator(
    task_id='sleep_even_more',
    bash_command='sleep 120',
    dag=dag
)

t1 >> email
email >> t2