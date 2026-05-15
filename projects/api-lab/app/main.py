from fastapi import FastAPI
from sqlalchemy import create_engine, text
from pydantic import BaseModel
from config import DATABASE_URL # <-- Importa la URL de la base de datos desde config.py que a su vez la obtiene de las variables de entorno del fich .env

### DATABASE_URL = "postgresql://lab_admin:j0s3l3@host.docker.internal:5432/lab_db"

engine = create_engine(DATABASE_URL)

app = FastAPI()


class Metric(BaseModel):
    source: str
    metric_value: float


@app.get("/")
def root():
    return {"message": "API funcionando"}


@app.get("/db")
def db_check():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        return {"database": str(result.fetchone())}


@app.post("/metrics")
def insert_metric(metric: Metric):

    query = text("""
        INSERT INTO metrics (source, metric_value)
        VALUES (:source, :metric_value)
    """)

    with engine.begin() as conn:
        conn.execute(
            query,
            {
                "source": metric.source,
                "metric_value": metric.metric_value
            }
        )

    return {"status": "inserted"}


@app.get("/metrics")
def get_metrics():

    query = text("""
        SELECT id, source, metric_value, created_at
        FROM metrics
        ORDER BY created_at DESC
        LIMIT 100
    """)

    with engine.connect() as conn:
        result = conn.execute(query)

        rows = []

        for row in result:
            rows.append({
                "id": row.id,
                "source": row.source,
                "metric_value": float(row.metric_value),
                "created_at": str(row.created_at)
            })

    return rows