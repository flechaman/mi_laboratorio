# Instalacion: Visual Studio Code

## Objetivo

Restaurar Visual Studio Code como entorno principal del laboratorio, incluyendo instalacion, configuracion, extensiones y sincronizacion con cuenta de GitHub.

## Requisitos

- Windows 11.
- WSL instalado.
- Repo clonado.
- Acceso a la cuenta de GitHub.

## Instalar VS Code

Desde PowerShell:

```powershell
winget install --id Microsoft.VisualStudioCode -e
```

Durante la instalacion, conviene activar:

- Agregar `code` al PATH.
- Registrar VS Code como editor para archivos soportados.
- Acciones de menu contextual si las quieres usar desde Windows.

Abre VS Code una vez para terminar la inicializacion.

## Restaurar configuracion del laboratorio

Desde PowerShell, en la raiz del repo:

```powershell
cd E:\Github\mi_laboratorio
powershell -ExecutionPolicy Bypass -File .\infra\vscode\restore-vscode.ps1
```

El script restaura:

- `settings.json`
- `chatLanguageModels.json`
- extensiones listadas en `infra/vscode/extensions.txt`
- snippets si existen en `infra/vscode/snippets`

## Extensiones restauradas

La lista versionada vive en:

```text
infra/vscode/extensions.txt
```

Incluye soporte para:

- Python y Pylance.
- Remote WSL.
- Docker/containers.
- Markdown Mermaid.
- C#/.NET.
- ChatGPT.
- Error Lens.
- idioma espanol.

## Abrir el repo desde WSL

Desde WSL:

```bash
cd /mnt/e/Github/mi_laboratorio
code .
```

Si `code` no existe:

1. Abre VS Code en Windows.
2. Pulsa `Ctrl+Shift+P`.
3. Ejecuta `Shell Command: Install 'code' command in PATH` si aparece.
4. Cierra y abre de nuevo la terminal.

## Sincronizacion con GitHub

En VS Code:

1. Abre el icono de cuentas abajo a la izquierda.
2. Elige `Turn on Settings Sync`.
3. Selecciona iniciar sesion con GitHub.
4. Autoriza VS Code en el navegador.
5. Activa al menos:
   - Settings.
   - Extensions.
   - Keybindings.
   - UI State si quieres replicar la experiencia visual.
   - Snippets si los usas.

Para un restore controlado, primero ejecuta `restore-vscode.ps1` y despues activa Settings Sync. Asi el estado versionado del repo queda como base.

## Verificacion

En PowerShell:

```powershell
code --version
code --list-extensions
```

En WSL:

```bash
cd /mnt/e/Github/mi_laboratorio
code .
```

Dentro de VS Code verifica:

- Abre una terminal WSL integrada.
- El prompt Starship se ve correctamente si lo instalaste.
- La extension Remote WSL esta instalada.
- Python detecta el interprete del virtualenv cuando lo crees.
- Git muestra la rama `master`.

## Actualizar el respaldo de VS Code

Si cambias extensiones o settings y quieres reflejarlo en el repo:

```powershell
code --list-extensions > .\infra\vscode\extensions.txt
copy $env:APPDATA\Code\User\settings.json .\infra\vscode\settings.json
```

Despues revisa el diff antes de commitear:

```bash
git diff infra/vscode
```

## Que no se respalda

No se versiona:

- `globalStorage`
- `workspaceStorage`
- `History`
- tokens o sesiones de extensiones
- caches locales

Esas carpetas pueden contener rutas locales, estado temporal o datos sensibles.

## Problemas habituales

- Si `code` no se reconoce, reinstala VS Code marcando PATH o abre VS Code una vez.
- Si Settings Sync pisa configuracion, revisa el historial de Settings Sync desde VS Code.
- Si Remote WSL no abre el repo, actualiza WSL y la extension `ms-vscode-remote.remote-wsl`.
