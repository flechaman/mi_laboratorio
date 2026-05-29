from datetime import datetime
from airflow.decorators import dag, task
from airflow.providers.amazon.aws.hooks.s3 import S3Hook


BUCKET_NAME = "bucket-lab"
CONN_ID = "minio_s3"


@dag(
    dag_id="dag_test_minio",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["lab", "minio", "bucket"],
)
def dag_test_minio():

    @task
    def subir_fichero():
        hook = S3Hook(aws_conn_id=CONN_ID)

        contenido = "Hola desde Airflow local hacia MinIO\n"
        key = "pruebas/fichero_airflow.txt"

        hook.load_string(
            string_data=contenido,
            key=key,
            bucket_name=BUCKET_NAME,
            replace=True,
        )

        print(f"Fichero subido: s3://{BUCKET_NAME}/{key}")
        return key

    @task
    def listar_bucket():
        hook = S3Hook(aws_conn_id=CONN_ID)

        keys = hook.list_keys(bucket_name=BUCKET_NAME) or []

        print("Contenido del bucket:")
        for key in keys:
            print(f"- {key}")

        return keys

    subir_fichero() >> listar_bucket()


dag_test_minio()
