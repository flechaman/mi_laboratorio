# Cobertura de instalacion

Matriz para comprobar si cada pieza del laboratorio tiene guia de restore.

| Componente | Ruta | Guia | Estado |
| --- | --- | --- | --- |
| Windows 11 + WSL | equipo base | `windows-wsl.md` | cubierto |
| Git + GitHub SSH | equipo base | `git-github-ssh.md` | cubierto |
| Docker Desktop + Compose | equipo base | `docker.md` | cubierto |
| Visual Studio Code | `infra/vscode` | `visual-studio-code.md` | cubierto |
| Python + pre-commit | repo raiz | `python.md` | cubierto |
| Starship | terminal | `starship.md` | cubierto |
| Airflow | `infra/airflow` | `airflow.md` | cubierto |
| PostgreSQL | `infra/core-stack`, `infra/airflow` | `postgresql.md` | cubierto |
| Redis | `infra/airflow` | `redis.md` | cubierto |
| MinIO | `infra/airflow` | `minio.md` | cubierto |
| Oracle Free | `infra/oracle` | `oracle.md` | cubierto |
| Grafana/Core Stack | `infra/core-stack`, `infra/grafana` | `core-stack-grafana.md` | cubierto |
| Azurite | `infra/storage/azurite` | `azurite.md` | cubierto |
| Azure Tools | Azure Functions/Azure CLI | `azure-tools.md` | cubierto |
| Mock API | `projects/mock-api` | `mock-api.md` | cubierto |
| API Lab | `projects/api-lab` | `api-lab.md` | cubierto |
| Azure Metrics Lab | `projects/azure_metrics_lab` | `azure-metrics-lab.md` | cubierto |
| Storage Lab | `projects/storage-lab` | `storage-lab.md` | cubierto |
| Gmail API | `infra/gmail-api`, `projects/gmail-ai-organizer` | `gmail-api.md` | cubierto |
| PowerBI | `infra/powerbi`, `projects/powerbi-datasets` | `powerbi.md` | cubierto |
| RAG local | `infra/rag`, `projects/ai-local-rag` | `rag.md` | cubierto |

## Regla

Si aparece una carpeta nueva en `infra/` o un proyecto funcional en `projects/`, debe tener:

- README operativo.
- Entrada en `docs/labs.md`.
- Entrada en esta matriz.
- Guia en `docs/install/` si requiere instalacion o configuracion no trivial.
