# Azure Metrics Function

Azure Function Python para recibir métricas, grabarlas en Azure Table Storage y persistir una copia JSONB en PostgreSQL.

## Configuracion

El archivo activo de Azure Functions es `local.settings.json`, pero no debe versionarse porque contiene secretos.

Plantilla disponible:

- `local.settings.azure.example.json`: entorno Azure con Storage Account y Azure Database for PostgreSQL.

Para preparar el entorno:

```bash
cp local.settings.azure.example.json local.settings.json
```

Después rellena los valores reales en `local.settings.json`.

## Variables clave

Azure Table Storage:

- `AZURE_STORAGE_CONNECTION_STRING`: connection string completa, preferida para Azure.
- `AzureWebJobsStorage`: también se acepta como connection string.
- `AZURE_STORAGE_ACCOUNT_NAME` y `AZURE_STORAGE_ACCESS_KEY`: alternativa cuando no se usa connection string completa.
- `AZURE_TABLE_NAME`: tabla destino.

PostgreSQL:

- `PG_HOST`, `PG_DATABASE`, `PG_USER`, `PG_PASSWORD`, `PG_PORT`, `PG_SSLMODE`, `PG_TABLE_NAME`.
- También se aceptan alias compatibles con Azure/PostgreSQL: `PGHOST`, `PGDATABASE`, `PGUSER`, `PGPASSWORD`, `PGPORT`, `PGSSLMODE`.

Para Azure PostgreSQL, usa normalmente:

```text
PG_SSLMODE=require
PG_TABLE_NAME=metrics_data
```

## Ejecutar

```bash
source .venv/bin/activate
func start
```
