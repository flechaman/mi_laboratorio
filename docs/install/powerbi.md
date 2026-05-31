# Instalacion: PowerBI

## Objetivo

Documentar la preparacion de los laboratorios PowerBI y datasets asociados.

## Rutas

```text
infra/powerbi/
projects/powerbi-datasets/
```

## Requisitos

- Power BI Desktop instalado en Windows si se van a abrir informes `.pbix`.
- Datasets o fuentes de datos disponibles localmente o en servicios externos.

## Instalacion

En Windows se puede instalar Power BI Desktop desde Microsoft Store o con instalador oficial.

Verifica:

```text
Power BI Desktop abre correctamente
```

## Convenciones del repo

No se versionan:

```text
*.pbix
*.pbit
```

Las plantillas, scripts y documentacion deben vivir en:

```text
projects/powerbi-datasets/
infra/powerbi/
```

## Notas

- Si un informe depende de datos locales, documenta la ruta y forma de regenerarlos.
- Si hay credenciales de origen de datos, se configuran fuera de Git.
