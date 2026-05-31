# Instalacion: Airflow

## Objetivo

Arrancar Airflow local con PostgreSQL, Redis, Celery Worker y MinIO usando Docker Compose.

## Requisitos

- Docker funcionando.
- Repo clonado en WSL.
- Plantilla de entorno creada.

## Preparar variables

```bash
cp infra/airflow/.env.example infra/airflow/.env
```

Revisa `infra/airflow/.env`.

## Construir y arrancar

Desde la raiz del repo:

```bash
make airflow-up
```

O directamente:

```bash
docker compose -f infra/airflow/docker-compose.yml up -d --build
```

## Verificacion

```bash
docker ps
docker compose -f infra/airflow/docker-compose.yml logs -f --tail=100
```

Accesos:

- Airflow: <http://localhost:8080>
- MinIO API: <http://localhost:9000>
- MinIO Console: <http://localhost:9001>

## Parar

```bash
make airflow-down
```

## Problemas habituales

- Si Airflow tarda en aparecer, espera a que `airflow-init` complete migraciones.
- Si el puerto `8080` esta ocupado, cambia el mapeo en `infra/airflow/docker-compose.yml`.
- No subas `logs/`, caches ni volumenes generados.
