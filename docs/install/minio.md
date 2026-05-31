# Instalacion: MinIO

## Objetivo

Reponer MinIO como almacenamiento S3-compatible local para pruebas, incluido dentro del stack de Airflow.

## Requisitos

- Docker funcionando.
- `infra/airflow/.env` creado.

## Arrancar

MinIO arranca junto con Airflow:

```bash
make airflow-up
```

## Accesos

- API: <http://localhost:9000>
- Consola: <http://localhost:9001>

Credenciales locales definidas en el compose:

```text
usuario: minioadmin
password: minioadmin
```

## Verificacion

```bash
docker ps
docker logs airflow-minio --tail=100
```

Abre la consola en el navegador:

```text
http://localhost:9001
```

## Parar

```bash
make airflow-down
```

## Notas

- Los datos de MinIO viven en el volumen Docker `minio-data`.
- No subas buckets ni datos reales al repo.
- Si un DAG depende de MinIO, documenta bucket y credenciales de laboratorio en el README del DAG o proyecto.
