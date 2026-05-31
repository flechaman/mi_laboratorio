# Guias de instalacion

Registro reproducible de como se instalo y configuro cada elemento del laboratorio.

El objetivo principal es poder **reponer el laboratorio desde cero** en un equipo nuevo o proporcionarselo a un compañero para que lo monte con el menor contexto posible.

## Ruta recomendada

| Guia | Uso |
| --- | --- |
| `reponer-laboratorio-desde-cero.md` | Checklist principal para reconstruir todo el laboratorio de principio a fin. |
| `cobertura.md` | Matriz de cobertura para saber que componentes tienen guia. |

## Entorno base

| Guia | Uso |
| --- | --- |
| `windows-wsl.md` | Preparar Windows 11, WSL y herramientas base. |
| `git-github-ssh.md` | Configurar Git, GitHub y autenticacion por SSH. |
| `docker.md` | Instalar y validar Docker Desktop/Compose. |
| `python.md` | Preparar Python, virtualenv, dependencias y pre-commit. |
| `starship.md` | Instalar Starship y fuente Nerd Font para el prompt. |
| `visual-studio-code.md` | Instalar VS Code, extensiones, configuracion y sincronizacion con GitHub. |

## Servicios e infraestructura

| Guia | Uso |
| --- | --- |
| `airflow.md` | Instalar y arrancar Airflow local con Docker. |
| `postgresql.md` | Reponer PostgreSQL local usado por Core Stack, Airflow y proyectos. |
| `minio.md` | Reponer MinIO local incluido en el stack de Airflow. |
| `redis.md` | Reponer Redis local usado por Airflow Celery. |
| `oracle.md` | Instalar Oracle Free local con Docker. |
| `core-stack-grafana.md` | Instalar stack base con PostgreSQL y Grafana. |
| `azurite.md` | Instalar Azurite para emular Azure Storage. |
| `azure-tools.md` | Instalar herramientas Azure locales usadas por los labs. |

## Proyectos

| Guia | Uso |
| --- | --- |
| `mock-api.md` | Arrancar Mock API con FastAPI y Docker. |
| `api-lab.md` | Arrancar API Lab con FastAPI y Docker. |
| `storage-lab.md` | Preparar Storage Lab con Python y Azure Blob/Azurite. |
| `azure-metrics-lab.md` | Preparar Azure Metrics Lab con Azure Functions y PostgreSQL. |
| `gmail-api.md` | Preparar laboratorios con Gmail API. |
| `powerbi.md` | Preparar laboratorios PowerBI y datasets. |
| `rag.md` | Preparar laboratorios RAG local. |

## Convenciones

- Cada guia debe incluir requisitos, pasos, verificacion y problemas habituales.
- Los secretos se documentan como nombres de variables, no como valores reales.
- Las rutas asumen WSL y este repositorio en `/mnt/e/Github/mi_laboratorio`.
- Si cambia un compose o README operativo, revisa la guia de instalacion correspondiente.
- La guia principal debe enlazar a las guias especificas, no duplicarlas por completo.
