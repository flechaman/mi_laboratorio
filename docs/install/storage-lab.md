# Instalacion: Storage Lab

## Objetivo

Preparar `projects/storage-lab` para probar subida y descarga de blobs.

## Requisitos

- Python 3.
- Storage real de Azure o Azurite.
- Dependencias de `requirements.txt`.

## Preparar entorno

```bash
cd projects/storage-lab
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Preparar Storage local

Si usas Azurite:

```bash
docker compose -f infra/storage/azurite/docker-compose.yml up -d
```

Consulta:

```text
docs/install/azurite.md
```

## Ejecutar

```bash
python upload_blob.py
python download_blob.py
```

## Notas

- No guardes connection strings reales en Git.
- `test.txt` y `downloaded_test.txt` son ficheros pequenos de prueba.
