# Oracle

Base de datos Oracle Free local para laboratorios.

## Requisitos

- Docker Desktop o Docker Engine con Compose.
- Cuenta aceptada en el registry de Oracle si la imagen lo requiere.
- Archivo `.env` creado a partir de `.env.example`.

## Configuracion

```bash
cp infra/oracle/.env.example infra/oracle/.env
```

Cambia `ORACLE_PWD` en `.env` antes de usarlo fuera de pruebas locales.

## Arrancar

Desde la raiz del repositorio:

```bash
make oracle-up
```

O directamente:

```bash
docker compose -f infra/oracle/docker-compose.yml up -d
```

## Puertos

- `1521`: listener Oracle.
- `5500`: Enterprise Manager Express.

## Parar

```bash
make oracle-down
```

## Notas

- Los datos viven en el volumen Docker `oracle-data`.
- Los scripts de inicializacion se pueden colocar en `infra/oracle/init/`.
- No subas dumps, wallets, credenciales ni datos reales.
