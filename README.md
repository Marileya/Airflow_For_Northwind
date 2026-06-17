## Airflow для БД Northwind
#### Проект на стадии работы

Данный проект основан на БД Northwind.
https://github.com/pthom/northwind_psql


Основная цель проекта - настроить DAG для взаимодействия с БД, выполнять базовые операции:
- извлечение информации,
- обработка,
- сохранение данных в MinIO.

#### Основной стек:
- python
- Airflow
- Celery/ Redis / Flower
- MinIO
- PostgreSQL / SQLAlchemy

Для безопасности используется две разных версии БД для самого предприятия Northwind и для Airflow.

#### Выполненные этапы:

- [x] Запуск Airflow на основе базового docker-compose файла (с офиц. сайта Airflow)
Проект использует CeleryExecuror вместе с БД Redis, для контроля за workers используется Flower 
- [x] Доработан docker_compose для запуска контейнеров Nortwhwind + pgAdmin
- [x] Внесена часть с MinIO
- [x] Созданы модели по БД с иcпользованием SQLAlchemy
- [x] Доработана сборка проекта в Dockerfile с упаковкой существующих файлов и установкой необходимых зависимостей
- [x] 
