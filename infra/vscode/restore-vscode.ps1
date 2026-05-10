$ErrorActionPreference = "Stop"

$backupRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$userConfig = Join-Path $env:APPDATA "Code\User"
$extensionsFile = Join-Path $backupRoot "extensions.txt"

New-Item -ItemType Directory -Force -Path $userConfig | Out-Null

$files = @(
    "settings.json",
    "chatLanguageModels.json"
)

foreach ($file in $files) {
    $source = Join-Path $backupRoot $file
    if (Test-Path $source) {
        Copy-Item -LiteralPath $source -Destination (Join-Path $userConfig $file) -Force
    }
}

$snippetsSource = Join-Path $backupRoot "snippets"
if (Test-Path $snippetsSource) {
    Copy-Item -LiteralPath $snippetsSource -Destination $userConfig -Recurse -Force
}

if (-not (Get-Command code -ErrorAction SilentlyContinue)) {
    Write-Warning "No encuentro el comando 'code'. Instala VS Code o agrégalo al PATH, y vuelve a ejecutar este script para instalar extensiones."
    exit 0
}

if (Test-Path $extensionsFile) {
    Get-Content $extensionsFile |
        Where-Object { $_ -and -not $_.StartsWith("#") } |
        ForEach-Object {
            Write-Host "Instalando extension $_"
            code --install-extension $_ --force
        }
}

Write-Host "Configuracion de VS Code restaurada."
