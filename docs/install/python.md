# Instalacion: Python y pre-commit

## Objetivo

Preparar Python para scripts, proyectos y checks del laboratorio.

## Entorno base en WSL

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
```

## Crear entorno virtual raiz

Desde la raiz del repo:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Instalar pre-commit

```bash
pip install pre-commit
pre-commit install
```

## Verificacion

```bash
python --version
pip --version
make test
make check
```

## Proyectos con dependencias propias

Algunos proyectos tienen su propio `requirements.txt`:

```text
projects/azure_metrics_lab/requirements.txt
projects/gmail-ai-organizer/requirements.txt
projects/storage-lab/requirements.txt
projects/api-lab/app/requirements.txt
projects/mock-api/app/requirements.txt
infra/airflow/requirements.txt
```

Instala dependencias dentro de un virtualenv cuando vayas a trabajar en cada proyecto.

## Problemas habituales

- En WSL puede existir `python3` pero no `python`; los comandos del repo usan fallback.
- No subas `.venv/` ni entornos virtuales al repositorio.
- Si un paquete falla compilando, actualiza `pip`, `setuptools` y `wheel`.
