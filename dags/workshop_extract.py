from datetime import timedelta

import airflow
from airflow import DAG
from workshop.postgres_to_file import PostgresToFileOperator

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': True,
    'start_date': airflow.utils.dates.days_ago(6),
    'email': ['airflow@example.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 0
}

dag = DAG(
    'workshop_extract',
    default_args=default_args,
    description='A simple extract demonstration DAG',
    schedule_interval=timedelta(days=1),
    template_searchpath='/usr/local/airflow/sql'
)

t1 = PostgresToFileOperator(
    sql='extract.sql',
    location='/usr/local/airflow/datalake/{{ds}}.json',
    conn_id='crm',
    task_id='extract',
    dag=dag
)
