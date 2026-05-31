# Instalacion: Core Stack y Grafana

## Objetivo

Arrancar el stack base local con PostgreSQL y Grafana.

## Requisitos

- Docker funcionando.
- Archivo `.env` en `infra/core-stack/`.

## Preparar variables

Si no existe, crea:

```bash
nano infra/core-stack/.env
```

Variables esperadas por el compose:

```env
POSTGRES_USER=lab
POSTGRES_PASSWORD=lab
POSTGRES_DB=lab
GRAFANA_ADMIN_USER=admin
GRAFANA_ADMIN_PASSWORD=admin
```

## Arrancar

```bash
make core-up
```

O directamente:

```bash
docker compose -f infra/core-stack/docker-compose.yml up -d
```

## Verificacion

```bash
docker ps
```

Accesos:

- PostgreSQL: `localhost:5432`
- Grafana: <http://localhost:3000>

## Parar

```bash
make core-down
```

## Problemas habituales

- Si Grafana no puede escribir, revisa permisos de `/home/jose/docker-data/grafana`.
- Si el puerto `5432` o `3000` esta ocupado, cambia el mapeo en el compose.
- No subas `grafana.db`, plugins descargados ni volumenes locales.
