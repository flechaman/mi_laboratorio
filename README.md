# Mi Laboratorio

Laboratorio personal profesional para experimentar, documentar y construir soluciones con Python, automatizacion, Azure, Docker, IA, Grafana, PowerBI, Gmail API y RAG local.

El objetivo de este repositorio es separar claramente pruebas, proyectos reutilizables, infraestructura, documentacion y area temporal de trabajo, manteniendo compatibilidad con Windows 11.

## Areas principales

| Carpeta | Uso |
| --- | --- |
| `projects/` | Proyectos completos o prototipos evolucionables. |
| `scripts/` | Scripts reutilizables, automatizaciones y pruebas historicas. |
| `infra/` | Servicios Docker, Azure, Grafana, Airflow, Oracle y configuracion reutilizable. |
| `docs/` | Notas, runbooks y documentacion operativa. |
| `notebooks/` | Exploracion de datos, IA y pruebas rapidas. |
| `data/` | Datos locales de entrada y salida. No guardar secretos ni datos sensibles. |
| `tests/` | Pruebas automatizadas compartidas. |
| `workspace/` | Area temporal ignorada por Git. |

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

## Comandos utiles

En Linux, WSL o Git Bash puedes usar:

```bash
make status
make airflow-up
make airflow-down
make core-up
make core-down
make oracle-up
make oracle-down
```

## Calidad y limpieza

Instala los hooks locales con:

```bash
pip install pre-commit
pre-commit install
```

Los hooks revisan formato basico, YAML/JSON, claves privadas accidentales y archivos grandes antes de cada commit.

## Convenciones

- Los scripts historicos se conservan en `scripts/python/learning/`.
- Cada proyecto futuro debe tener su propio `README.md`, `.env.example` si aplica y notas de ejecucion.
- Los secretos reales van en `.env`, nunca en Git.
- La configuracion reutilizable vive en `infra/`.
- Los datos grandes, temporales o sensibles no se versionan.
- Los artefactos generados (`*.zip`, logs, caches, volumenes Docker) se quedan fuera de Git salvo excepcion documentada.

## Proyectos sugeridos

- Automatizacion de tareas locales con Python y PowerShell.
- Laboratorio Docker para servicios auxiliares.
- RAG local con embeddings, vector store y documentos propios.
- Dashboards de Grafana con Prometheus.
- Datasets limpios para PowerBI.
- Integracion con Gmail API para clasificacion y automatizacion de correo.
- Pruebas de despliegue y automatizacion en Azure.
