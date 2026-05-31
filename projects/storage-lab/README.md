# Storage Lab

Laboratorio Python para probar subida y descarga de blobs.

## Requisitos

- Python 3.
- Dependencias de `requirements.txt`.
- Variables de conexion al storage configuradas en entorno local.

## Preparar entorno

```bash
cd projects/storage-lab
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Ejecutar

```bash
python upload_blob.py
python download_blob.py
```

## Notas

- `test.txt` y `downloaded_test.txt` son ficheros de prueba pequenos.
- No subas credenciales ni connection strings reales.
