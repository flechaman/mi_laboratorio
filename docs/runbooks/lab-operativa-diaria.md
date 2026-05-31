# Operativa diaria del laboratorio

Guia breve para abrir, revisar y cerrar una sesion de trabajo.

## Inicio

```bash
cd /mnt/e/Github/mi_laboratorio
git status --short --branch
make check
```

Si vas a trabajar con servicios Docker:

```bash
docker compose version
docker ps
```

## Servicios habituales

| Servicio | Comando | URL o puerto |
| --- | --- | --- |
| Airflow | `make airflow-up` | <http://localhost:8080> |
| MinIO API | `make airflow-up` | <http://localhost:9000> |
| MinIO Console | `make airflow-up` | <http://localhost:9001> |
| Oracle | `make oracle-up` | `localhost:1521` |
| Grafana/Core | `make core-up` | Revisar compose de `infra/core-stack` |
| Mock API | `docker compose -f projects/mock-api/docker-compose.yml up -d --build` | <http://localhost:8001/docs> |

## Cierre

Antes de cerrar una sesion:

```bash
git status --short --branch
make test
```

Para parar servicios:

```bash
make airflow-down
make core-down
make oracle-down
```

## Antes de commitear

```bash
git status --short
git diff --check
make test
```

Evita versionar:

- `.env`, `local.settings.json` y credenciales.
- Logs, caches y `__pycache__/`.
- Volumenes Docker y bases de datos locales.
- Artefactos generados como `*.zip`.
