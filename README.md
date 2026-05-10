# Mi Laboratorio

Laboratorio personal profesional para experimentar, documentar y construir soluciones con Python, automatizacion, Azure, Docker, IA, Grafana, PowerBI, Gmail API y RAG local.

El objetivo de este repositorio es separar claramente pruebas, proyectos reutilizables, infraestructura, documentacion y area temporal de trabajo, manteniendo compatibilidad con Windows 11.

## Areas principales

- `projects/`: proyectos completos o prototipos evolucionables.
- `scripts/`: scripts reutilizables, automatizaciones y pruebas historicas.
- `infra/`: configuracion de Docker, Azure, Grafana, RAG local y servicios externos.
- `docs/`: notas, runbooks y documentacion operativa.
- `notebooks/`: exploracion de datos, IA y pruebas rapidas.
- `data/`: datos locales de entrada y salida. No guardar secretos ni datos sensibles.
- `tests/`: pruebas automatizadas compartidas.
- `workspace/`: area temporal ignorada por Git.

## Primeros pasos en Windows 11

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
copy .env.example .env
```

Para levantar los servicios iniciales:

```powershell
docker compose up -d
```

## Convenciones

- Los scripts historicos se conservan en `scripts/python/learning/`.
- Cada proyecto futuro debe tener su propio `README.md`, `.env.example` si aplica y notas de ejecucion.
- Los secretos reales van en `.env`, nunca en Git.
- La configuracion reutilizable vive en `infra/`.
- Los datos grandes, temporales o sensibles no se versionan.

## Proyectos sugeridos

- Automatizacion de tareas locales con Python y PowerShell.
- Laboratorio Docker para servicios auxiliares.
- RAG local con embeddings, vector store y documentos propios.
- Dashboards de Grafana con Prometheus.
- Datasets limpios para PowerBI.
- Integracion con Gmail API para clasificacion y automatizacion de correo.
- Pruebas de despliegue y automatizacion en Azure.
