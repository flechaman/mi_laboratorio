# Instalacion: Azure Metrics Lab

## Objetivo

Preparar la Azure Function Python que recibe metricas, escribe en Azure Table Storage y guarda copia en PostgreSQL.

## Requisitos

- Python 3.
- Azure Functions Core Tools si vas a ejecutar `func start`.
- Acceso a Azure Storage o Azurite.
- PostgreSQL local o Azure Database for PostgreSQL.

## Preparar entorno Python

```bash
cd projects/azure_metrics_lab
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Preparar configuracion

```bash
cp local.settings.azure.example.json local.settings.json
```

Edita `local.settings.json` con tus valores reales.

Variables clave:

- `AZURE_STORAGE_CONNECTION_STRING`
- `AZURE_TABLE_NAME`
- `PG_HOST`
- `PG_DATABASE`
- `PG_USER`
- `PG_PASSWORD`
- `PG_PORT`
- `PG_SSLMODE`
- `PG_TABLE_NAME`

## Arrancar

```bash
func start
```

## Verificacion

```bash
curl -X POST http://localhost:7071/api/<endpoint> \
  -H "Content-Type: application/json" \
  -d @samples/e2e_correos_payload.json
```

Ajusta `<endpoint>` al nombre real de la funcion.

## Problemas habituales

- `local.settings.json` no debe versionarse.
- Para Azure PostgreSQL normalmente usa `PG_SSLMODE=require`.
- Si falla Storage, prueba primero con Azurite o revisa la connection string.
