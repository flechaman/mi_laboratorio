# Windows 11 Setup

Guia base para preparar el laboratorio en Windows 11.

## Requisitos

- Git for Windows.
- Python 3.11 o superior.
- Docker Desktop si se van a usar servicios locales.
- PowerShell 5.1 o PowerShell 7.

## Entorno Python

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Variables de entorno

```powershell
copy .env.example .env
notepad .env
```

## Docker

```powershell
docker compose --profile data up -d
docker compose --profile observability up -d
docker compose --profile rag up -d
```

## Verificacion

```powershell
python --version
pip list
git status
```
