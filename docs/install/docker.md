# Instalacion: Docker

## Objetivo

Instalar Docker Desktop y validar Docker Compose para levantar los servicios del laboratorio.

## Windows 11

Instala Docker Desktop desde la web oficial y activa la integracion con WSL.

En Docker Desktop:

```text
Settings -> Resources -> WSL Integration
```

Activa la distribucion Linux que uses.

## Verificacion en WSL

```bash
docker --version
docker compose version
docker ps
```

## Probar con servicios del laboratorio

```bash
make core-up
docker ps
make core-down
```

## Convenciones del repo

- Los `docker-compose.yml` versionados son configuracion.
- Los volumenes, logs y bases de datos locales no se versionan.
- Las variables reales van en `.env`; las plantillas van en `.env.example`.

## Problemas habituales

- Si `docker ps` no responde, revisa que Docker Desktop este abierto.
- Si WSL no ve Docker, revisa la integracion WSL en Docker Desktop.
- Si un puerto esta ocupado, cambia el mapeo en el compose o para el servicio que lo usa.
