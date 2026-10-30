from datetime import datetime
from airflow.sdk import dag, task
from generating_config import generating_config_file
from fetch_image import fetch_image_file

@dag(
    dag_id="solar_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=['solar', 'config_file_generator'],
)
def solar_pipeline():

    @task(task_id="generating_config")
    def generate_config_files():
        generating_config_file()

    @task(task_id="fetch_image")
    def fetch_image_files():
        fetch_image_file()

    generate_config_files() >> fetch_image_files()

solar_pipeline()