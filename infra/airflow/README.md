# Airflow

Stack local de Apache Airflow con PostgreSQL, Redis, worker Celery y MinIO para pruebas de DAGs.

## Requisitos

- Docker Desktop o Docker Engine con Compose.
- Archivo `.env` creado a partir de `.env.example`.

## Configuracion

```bash
cp infra/airflow/.env.example infra/airflow/.env
```

Revisa los valores antes de arrancar. Los valores incluidos son solo para laboratorio local.

## Arrancar

Desde la raiz del repositorio:

```bash
make airflow-up
```

O directamente:

```bash
docker compose -f infra/airflow/docker-compose.yml up -d
```

## Accesos

- Airflow: <http://localhost:8080>
- MinIO API: <http://localhost:9000>
- MinIO Console: <http://localhost:9001>

## Parar

```bash
make airflow-down
```

## Notas

- `logs/`, `__pycache__/`, volumenes y ficheros generados no deben versionarse.
- Los DAGs reutilizables viven en `dags/`.
- `plugins/` y `config/` quedan preparados para extensiones futuras.
