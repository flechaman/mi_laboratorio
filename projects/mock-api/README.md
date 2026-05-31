# Mock API

Mock API basada en FastAPI para simular servicios externos y probar automatismos locales sin depender de sistemas reales.

## Arrancar

Desde la raiz del repositorio:

```bash
docker compose -f projects/mock-api/docker-compose.yml up -d --build
```

## Accesos

- Swagger: <http://localhost:8001/docs>
- OpenAPI: <http://localhost:8001/openapi.json>
- Health: <http://localhost:8001/health>

## Ejemplos

```bash
curl http://localhost:8001/health
curl http://localhost:8001/saldo/600000001
```

```bash
curl -X POST http://localhost:8001/recarga \
  -H "Content-Type: application/json" \
  -d '{"msisdn":"600000002","amount":0.20,"reason":"DAG AIRPR0543"}'
```

## Parar

```bash
docker compose -f projects/mock-api/docker-compose.yml down
```

## Documentacion historica

El detalle ampliado esta en `README_mock_api.md`.
