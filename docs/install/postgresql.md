# Instalacion: PostgreSQL

## Objetivo

Reponer PostgreSQL local para laboratorios que necesitan base de datos relacional.

En este repo PostgreSQL se usa principalmente de dos formas:

- `infra/core-stack/docker-compose.yml`: PostgreSQL general del laboratorio en `localhost:5432`.
- `infra/airflow/docker-compose.yml`: PostgreSQL interno de Airflow, aislado dentro de su red Docker.

## Requisitos

- Docker funcionando.
- Variables locales creadas en `.env` cuando el compose las requiera.

## PostgreSQL del Core Stack

Prepara `infra/core-stack/.env`:

```env
POSTGRES_USER=lab
POSTGRES_PASSWORD=lab
POSTGRES_DB=lab
GRAFANA_ADMIN_USER=admin
GRAFANA_ADMIN_PASSWORD=admin
```

Arranca:

```bash
make core-up
```

Verifica:

```bash
docker ps
docker logs lab-postgres --tail=100
```

Conexion:

```text
host: localhost
port: 5432
database: lab
user: lab
password: lab
```

## PostgreSQL de Airflow

Arranca con:

```bash
make airflow-up
```

Este PostgreSQL esta pensado para metadatos de Airflow, no para uso general.

## Parar

```bash
make core-down
make airflow-down
```

## Notas

- Los datos viven en volumenes Docker.
- No subas dumps ni bases de datos locales.
- Si necesitas backup real, guardalo fuera del repo o en un sistema seguro.
