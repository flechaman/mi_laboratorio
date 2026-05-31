# API Lab

Laboratorio FastAPI con contenedor Docker y servicio auxiliar de base de datos para pruebas locales de APIs.

## Requisitos

- Docker Desktop o Docker Engine con Compose.
- Archivo `.env` local si el compose o la aplicacion lo requieren.

## Arrancar

Desde la raiz del repositorio:

```bash
docker compose -f projects/api-lab/docker-compose.yml up -d --build
```

## Parar

```bash
docker compose -f projects/api-lab/docker-compose.yml down
```

## Estructura

- `app/main.py`: aplicacion principal.
- `app/config.py`: configuracion.
- `app/db.py`: acceso a base de datos.
- `metric_generator.py`: generador local de metricas.

## Notas

- No subas `.env`, caches ni datos generados.
- Si el laboratorio madura, anade `.env.example` con las variables necesarias.
