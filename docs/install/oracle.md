# Instalacion: Oracle Free

## Objetivo

Arrancar Oracle Free local para pruebas con bases de datos.

## Requisitos

- Docker funcionando.
- Acceso a la imagen `container-registry.oracle.com/database/free:latest`.
- Archivo `.env` local.

## Preparar variables

```bash
cp infra/oracle/.env.example infra/oracle/.env
```

Cambia `ORACLE_PWD` si vas a usarlo fuera de pruebas locales.

## Arrancar

```bash
make oracle-up
```

O directamente:

```bash
docker compose -f infra/oracle/docker-compose.yml up -d
```

## Verificacion

```bash
docker ps
docker logs lab-oracle --tail=100
```

Puertos:

- `1521`: listener Oracle.
- `5500`: Enterprise Manager Express.

## Parar

```bash
make oracle-down
```

## Problemas habituales

- La primera inicializacion puede tardar varios minutos.
- Si falla la descarga de la imagen, revisa acceso al registry de Oracle.
- No subas dumps, wallets, datos reales ni credenciales.
