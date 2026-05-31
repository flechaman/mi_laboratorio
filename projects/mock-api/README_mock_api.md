# Mock API - Laboratorio Local

## Objetivo

Mock API basada en FastAPI para simular servicios externos y probar automatismos locales sin depender de sistemas reales.

Permite ser consumida desde:

- Airflow
- Azure Functions
- Scripts Python
- Bash / curl
- Pruebas de integración
- Grafana (a través de procesos que consuman la API)

---

## Estructura

```text
projects/mock-api
├── Dockerfile
├── docker-compose.yml
├── README.md
└── app
    ├── main.py
    └── requirements.txt
```

---

## Arranque

```bash
cd /mnt/e/Github/mi_laboratorio/projects/mock-api

docker compose up -d --build
```

Verificar:

```bash
docker ps
```

---

## Swagger

Documentación automática:

http://localhost:8001/docs

OpenAPI:

http://localhost:8001/openapi.json

---

## Health Check

### Request

```bash
curl http://localhost:8001/health
```

### Respuesta

```json
{
  "status": "UP",
  "timestamp": "2026-05-31T12:00:00"
}
```

---

## Consulta de saldo

### Request

```bash
curl http://localhost:8001/saldo/600000001
```

### Respuesta

```json
{
  "msisdn": "600000001",
  "saldo": 10.5,
  "estado": "OK",
  "timestamp": "2026-05-31T12:00:00"
}
```

---

## Recarga simulada

### Request

```bash
curl -X POST http://localhost:8001/recarga \
  -H "Content-Type: application/json" \
  -d '{
        "msisdn":"600000002",
        "amount":0.20,
        "reason":"DAG AIRPR0543"
      }'
```

### Respuesta

```json
{
  "estado": "OK",
  "mensaje": "Recarga simulada correctamente",
  "msisdn": "600000002",
  "saldo_anterior": 0.10,
  "importe_recarga": 0.20,
  "saldo_nuevo": 0.30
}
```

---

## Activación de bono

### Request

```bash
curl -X POST http://localhost:8001/bono \
  -H "Content-Type: application/json" \
  -d '{
        "msisdn":"600000002",
        "product_offering_id":"PO_TODO_INCLUIDO_15_Lebara",
        "sales_person_id":"DAG AIRPR0543"
      }'
```

### Respuesta

```json
{
  "estado": "OK",
  "mensaje": "Bono activado correctamente",
  "msisdn": "600000002",
  "product_offering_id": "PO_TODO_INCLUIDO_15_Lebara"
}
```

---

## Consulta de bonos activos

### Request

```bash
curl http://localhost:8001/bono/600000002
```

### Respuesta

```json
{
  "msisdn": "600000002",
  "bonos_activos": [
    "PO_TODO_INCLUIDO_15_Lebara"
  ]
}
```

---

## Uso desde Airflow

Dentro de contenedores Docker:

```python
MOCK_API_BASE_URL = "http://host.docker.internal:8001"
```

Ejemplo:

```python
import requests

response = requests.get(
    f"{MOCK_API_BASE_URL}/saldo/600000001"
)

print(response.json())
```

---

## Casos de uso previstos

### Simulación de recargas

- Qvantel
- Prepago
- Procesos masivos

### Simulación de activación de bonos

- Lebara
- Llamaya
- Orange
- MásMóvil

### Pruebas Airflow

- HttpOperator
- PythonOperator
- BranchPythonOperator

### Pruebas Azure Functions

- Integraciones REST
- Reintentos
- Manejo de errores

---

## Mejoras futuras

- Persistencia en PostgreSQL
- Persistencia en Azurite Table Storage
- Simulación de errores aleatorios
- Delays configurables
- Autenticación JWT
- Catálogo de MSISDNs configurable
- Escenarios parametrizados por fichero JSON
- Métricas Prometheus
- Dashboards Grafana
