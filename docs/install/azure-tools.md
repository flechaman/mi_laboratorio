# Instalacion: herramientas Azure

## Objetivo

Preparar herramientas locales para laboratorios con Azure Functions, Azure Storage, Azure Table y Azurite.

## Herramientas habituales

- Azure CLI.
- Azure Functions Core Tools.
- Azurite si se quiere emular Storage localmente.
- Extension de Azure para VS Code si se usa desde el editor.

## Azure CLI

En Windows se puede instalar con `winget`:

```powershell
winget install --id Microsoft.AzureCLI -e
```

Verifica:

```powershell
az version
az login
```

## Azure Functions Core Tools

En Windows se puede instalar con `winget`:

```powershell
winget install --id Microsoft.Azure.FunctionsCoreTools -e
```

Verifica:

```powershell
func --version
```

## Azurite

Para Azurite usa la guia:

```text
docs/install/azurite.md
```

## Variables

Los proyectos no deben guardar secretos reales. Usa plantillas:

```text
projects/azure_metrics_lab/local.settings.azure.example.json
```

El archivo real es:

```text
projects/azure_metrics_lab/local.settings.json
```

y no se versiona.

## Problemas habituales

- Si `func` no se reconoce, abre una nueva terminal tras instalar.
- Si `az login` falla, revisa navegador, proxy o permisos corporativos.
- Si usas WSL, puede ser mas simple ejecutar `az` y `func` desde Windows PowerShell y el codigo desde VS Code/WSL.
