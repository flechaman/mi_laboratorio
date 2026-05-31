# Instalacion: Mock API

## Objetivo

Arrancar la Mock API basada en FastAPI para simular servicios externos.

## Requisitos

- Docker funcionando.
- Proyecto `projects/mock-api`.

## Arrancar

```bash
docker compose -f projects/mock-api/docker-compose.yml up -d --build
```

## Verificacion

```bash
docker ps
curl http://localhost:8001/health
```

Accesos:

- Swagger: <http://localhost:8001/docs>
- OpenAPI: <http://localhost:8001/openapi.json>

## Parar

```bash
docker compose -f projects/mock-api/docker-compose.yml down
```

## Problemas habituales

- Si `8001` esta ocupado, cambia el puerto externo del compose.
- Revisa `projects/mock-api/README.md` y `README_mock_api.md` para ejemplos de endpoints.
