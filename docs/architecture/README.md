# Arquitectura del laboratorio

Este directorio recoge decisiones y mapas tecnicos de alto nivel.

## Mapa general

```text
projects/      Laboratorios y prototipos con objetivo concreto
infra/         Servicios reutilizables y stacks Docker
scripts/       Automatizaciones y utilidades
docs/          Runbooks, notas y arquitectura
data/          Datos locales pequenos o plantillas
tests/         Comprobaciones automatizadas del repositorio
workspace/     Area temporal ignorada por Git
```

## Principios

- La infraestructura reutilizable vive en `infra/`.
- Los proyectos consumen servicios de `infra/` cuando tiene sentido.
- Los secretos se documentan como `.env.example`, pero los valores reales no se versionan.
- Los datos generados y volumenes locales se regeneran, no se suben.
- Cada lab funcional debe poder arrancarse con instrucciones desde su README.

## Flujos principales

- Airflow puede orquestar pruebas contra MinIO, Mock API y otros servicios internos.
- `azure_metrics_lab` concentra pruebas de ingesta y persistencia de metricas.
- `core-stack` agrupa servicios auxiliares de observabilidad y almacenamiento local.
- `scripts/` conserva automatizaciones reutilizables o historicas.
