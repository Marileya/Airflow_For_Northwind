from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime
import time
import os


def check_connection():
    pg_hook = PostgresHook(
        postgres_conn_id='northwind',
        hook_params={"enable_log_db_messages": True},
    )
    try:
        with pg_hook.get_conn() as pg_conn:
            with pg_conn.cursor() as cursor:
                cursor.execute("SELECT category_name FROM categories WHERE category_id = 6;")
                result = cursor.fetchone()
                print(f"Category name: {result}")
    except Exception as e:
        print(f"Connection failed: {e}")


def testing():
    now = datetime.now()
    print(f"Сегодня: {now}")
    return now


with DAG(
    dag_id='postgres_connecting',
    start_date=datetime(2026, 4, 1),
    schedule=None,
    catchup=False
) as dag:
    connection_check = PythonOperator(
        task_id='check_connection_task',
        python_callable=check_connection,
    )

    call_proc = SQLExecuteQueryOperator(
        task_id="call_proc",
        conn_id="northwind",
        sql="SELECT category_name FROM categories WHERE category_id = 6;",
        hook_params={"enable_log_db_messages": True},
    )

    testing_python = PythonOperator(
        task_id='python',
        python_callable=testing
    )

connection_check >> call_proc >> testing_python
