FROM apache/airflow:3.2.1

WORKDIR /opt/airflow

RUN mkdir -p dags logs plugins config


COPY requirements.txt .
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r requirements.txt

COPY northwind.sql .

COPY --chown=airflow:root dags/ ./dags/
COPY --chown=airflow:root plugins/ ./plugins/
COPY --chown=airflow:root config/ ./config/
COPY --chown=airflow:root src/ ./src/

USER airflow

# RUN chown -R airflow:root /opt/airflow

# RUN chmod -R 755 /opt/airflow
