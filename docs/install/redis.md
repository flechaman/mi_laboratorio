# Instalacion: Redis

## Objetivo

Reponer Redis local usado por Airflow como broker Celery.

## Requisitos

- Docker funcionando.
- Stack de Airflow preparado.

## Arrancar

Redis arranca dentro del stack de Airflow:

```bash
make airflow-up
```

## Verificacion

```bash
docker ps
docker logs airflow-redis --tail=100
```

Desde otros contenedores de la red de Airflow se usa:

```text
redis://airflow-redis:6379/0
```

## Parar

```bash
make airflow-down
```

## Notas

- Este Redis es infraestructura interna de Airflow.
- No esta pensado como Redis general del laboratorio salvo que lo documentes expresamente.
