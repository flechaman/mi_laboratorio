from datetime import datetime

from airflow.decorators import dag, task


@dag(
    dag_id="dag_test_lab",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["lab", "test"],
)
def dag_test_lab():

    @task
    def inicio():
        print("Airflow local funcionando correctamente")
        return "OK"

    @task
    def fin(resultado):
        print(f"Resultado recibido: {resultado}")

    fin(inicio())


dag_test_lab()
