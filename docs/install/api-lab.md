# Instalacion: API Lab

## Objetivo

Arrancar `projects/api-lab`, laboratorio FastAPI con Docker para pruebas de API y base de datos.

## Requisitos

- Docker funcionando.
- Proyecto `projects/api-lab`.

## Arrancar

```bash
docker compose -f projects/api-lab/docker-compose.yml up -d --build
```

## Verificacion

```bash
docker ps
docker compose -f projects/api-lab/docker-compose.yml logs --tail=100
```

## Parar

```bash
docker compose -f projects/api-lab/docker-compose.yml down
```

## Notas

- No subas `.env` locales ni `.venv/`.
- Si el proyecto madura, crea `.env.example` con variables necesarias.
- Documenta puertos y endpoints en `projects/api-lab/README.md`.
