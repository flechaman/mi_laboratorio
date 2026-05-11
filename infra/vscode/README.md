# Respaldo de Visual Studio Code

Respaldo creado antes de reinstalar Windows.

Incluye:

- `settings.json`: preferencias principales de VS Code.
- `chatLanguageModels.json`: configuración visible de modelos de chat.
- `extensions.txt`: extensiones instalables desde el Marketplace.
- `restore-vscode.ps1`: script para restaurar configuración y extensiones.

No incluye `globalStorage`, `workspaceStorage` ni `History`, porque pueden contener estado temporal, rutas locales o datos sensibles de extensiones.

## Restaurar en Windows

Instala Visual Studio Code y abre PowerShell en la raíz de este repositorio:

```powershell
powershell -ExecutionPolicy Bypass -File .\infra\vscode\restore-vscode.ps1
```

Si el comando `code` no existe después de instalar VS Code, abre VS Code una vez o reinstálalo marcando la opción de agregarlo al PATH.
