# Indice de laboratorios

Resumen operativo de los laboratorios del repositorio.

| Lab | Estado | Tecnologia | Ruta | Arranque |
| --- | --- | --- | --- | --- |
| Airflow | experimental | Airflow, PostgreSQL, Redis, MinIO | `infra/airflow` | `make airflow-up` |
| Core Stack | experimental | Grafana, PostgreSQL, servicios base | `infra/core-stack` | `make core-up` |
| Oracle | experimental | Oracle Free, Docker | `infra/oracle` | `make oracle-up` |
| Azure Metrics Lab | funcional | Azure Functions, Azure Table, PostgreSQL | `projects/azure_metrics_lab` | Ver README |
| Mock API | funcional | FastAPI, Docker | `projects/mock-api` | `docker compose -f projects/mock-api/docker-compose.yml up -d --build` |
| API Lab | experimental | FastAPI, PostgreSQL, Docker | `projects/api-lab` | `docker compose -f projects/api-lab/docker-compose.yml up -d --build` |
| Storage Lab | experimental | Azure Blob Storage, Python | `projects/storage-lab` | Ver README |
| Gmail AI Organizer | idea | Gmail API, Python, IA | `projects/gmail-ai-organizer` | Ver README |
| AI Local RAG | idea | RAG local, embeddings | `projects/ai-local-rag` | Ver README |
| Grafana Observability | idea | Grafana, Prometheus | `projects/grafana-observability` | Ver README |
| PowerBI Datasets | idea | PowerBI, datasets | `projects/powerbi-datasets` | Ver README |

## Estados

- `idea`: carpeta preparada, pendiente de implementacion.
- `experimental`: funciona como laboratorio, puede cambiar con frecuencia.
- `funcional`: tiene flujo de uso definido y README operativo.
- `estable`: listo para uso repetido con pocas modificaciones.
- `archivado`: conservado como referencia historica.

## Regla de mantenimiento

Cada lab que pase a `funcional` debe tener:

- `README.md` con objetivo, requisitos y comandos.
- `.env.example` si usa variables o secretos.
- `requirements.txt`, `Dockerfile` o `docker-compose.yml` cuando aplique.
- Notas de puertos y problemas habituales.
