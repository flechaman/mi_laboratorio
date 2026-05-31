# Guias de instalacion

Registro reproducible de como se instalo y configuro cada elemento del laboratorio.

## Entorno base

| Guia | Uso |
| --- | --- |
| `windows-wsl.md` | Preparar Windows 11, WSL y herramientas base. |
| `git-github-ssh.md` | Configurar Git, GitHub y autenticacion por SSH. |
| `docker.md` | Instalar y validar Docker Desktop/Compose. |
| `python.md` | Preparar Python, virtualenv, dependencias y pre-commit. |
| `starship.md` | Instalar Starship y fuente Nerd Font para el prompt. |

## Servicios e infraestructura

| Guia | Uso |
| --- | --- |
| `airflow.md` | Instalar y arrancar Airflow local con Docker. |
| `oracle.md` | Instalar Oracle Free local con Docker. |
| `core-stack-grafana.md` | Instalar stack base con PostgreSQL y Grafana. |
| `azurite.md` | Instalar Azurite para emular Azure Storage. |

## Proyectos

| Guia | Uso |
| --- | --- |
| `mock-api.md` | Arrancar Mock API con FastAPI y Docker. |
| `azure-metrics-lab.md` | Preparar Azure Metrics Lab con Azure Functions y PostgreSQL. |

## Convenciones

- Cada guia debe incluir requisitos, pasos, verificacion y problemas habituales.
- Los secretos se documentan como nombres de variables, no como valores reales.
- Las rutas asumen WSL y este repositorio en `/mnt/e/Github/mi_laboratorio`.
- Si cambia un compose o README operativo, revisa la guia de instalacion correspondiente.
