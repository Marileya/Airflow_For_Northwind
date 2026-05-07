from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.common.sql.operators.sql import SQLValueCheckOperator
from datetime import datetime, timedelta


with DAG(
    'postgres_value',
    description='DAG to postgres',
    start_date=datetime(2026, 4, 25),
    schedule=None,
    catchup=False,
) as dag:
    task1 = SQLValueCheckOperator(
        task_id='test_dag1',
        conn_id='northwind',
        sql='SELECT count(*) FROM categories;',
        pass_value=5,
        tolerance=1
    )

    task1
