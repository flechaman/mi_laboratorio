# Instalacion: Gmail API

## Objetivo

Preparar los laboratorios relacionados con Gmail API y organizacion automatizada de correo.

## Rutas

```text
infra/gmail-api/
projects/gmail-ai-organizer/
```

## Requisitos

- Python 3.
- Proyecto de Google Cloud con Gmail API habilitada si se usa API real.
- Credenciales OAuth descargadas fuera del repositorio.

## Preparar Python

```bash
cd projects/gmail-ai-organizer
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Credenciales

No se versionan:

```text
credentials.json
token.json
```

Estan ignoradas por `.gitignore`.

## Verificacion

```bash
python --version
pip list
```

Cuando exista script principal, documenta el comando exacto en `projects/gmail-ai-organizer/README.md`.

## Notas

- No compartas tokens OAuth por Git.
- Para entregar el laboratorio a un compañero, debe crear sus propias credenciales Google.
