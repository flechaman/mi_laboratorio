# Instalacion: Azurite

## Objetivo

Arrancar Azurite como emulador local de Azure Storage.

## Requisitos

- Docker funcionando.
- Compose de `infra/storage/azurite`.

## Arrancar

```bash
docker compose -f infra/storage/azurite/docker-compose.yml up -d
```

## Verificacion

```bash
docker ps
docker compose -f infra/storage/azurite/docker-compose.yml logs --tail=100
```

## Uso esperado

Configura tus proyectos para apuntar al endpoint local de Azurite cuando no quieras usar Azure real.

## Parar

```bash
docker compose -f infra/storage/azurite/docker-compose.yml down
```

## Problemas habituales

- Si un puerto esta ocupado, revisa el compose de Azurite.
- Mantener datos de prueba locales fuera de Git.
