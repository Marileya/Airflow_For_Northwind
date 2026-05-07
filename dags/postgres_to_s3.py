from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from datetime import datetime
import csv
import os


BUCKET_NAME = "airflow-bucket"
KEY_NAME = f"categories_export_{datetime.now()}.csv"


def export_postgres_to_s3(ds, **kwargs):
    pg_hook = PostgresHook(postgres_conn_id="northwind")
    connection = pg_hook.get_conn()
    cursor = connection.cursor()
    cursor.execute("SELECT category_id, category_name, description FROM categories;")
    results = cursor.fetchall()

    local_filename = f"/tmp/categories_{ds}.csv"

    with open(local_filename, 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['category_id', 'category_name', 'description'])
        csv_writer.writerows(results)

    print(f"Данные выгружены локально: {local_filename}")

    s3_hook = S3Hook(aws_conn_id="minio_s3")

    s3_hook.load_file(
        filename=local_filename,
        key=KEY_NAME,
        bucket_name=BUCKET_NAME,
        replace=True
    )

    print(f"Файл успешно загружен в S3: {BUCKET_NAME}/{KEY_NAME}")

    os.remove(local_filename)


with DAG(
    dag_id="export_to_datalake",
    start_date=datetime(2026, 4, 28),
    schedule=None,
    catchup=False
) as dag:

    upload_task = PythonOperator(
        task_id="upload_to_s3",
        python_callable=export_postgres_to_s3
    )
