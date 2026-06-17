from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
import asyncio
from src.core.db import check_connection


def testing():
    asyncio.run(check_connection())


with DAG(
    dag_id="sqlalchemy_test",
    start_date=datetime(2026, 4, 28),
    schedule=None,
    catchup=False
) as dag:

    task_SQLAl = PythonOperator(
        task_id="sqlalchemy_test",
        python_callable=testing
    )
