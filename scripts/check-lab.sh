#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "== Git =="
git status --short --branch

echo
echo "== Herramientas =="
PYTHON_BIN="$(command -v python3 || command -v python || true)"
if [[ -n "$PYTHON_BIN" ]]; then
  "$PYTHON_BIN" --version
else
  echo "python no encontrado"
  exit 1
fi
if command -v docker >/dev/null 2>&1; then
  docker --version
else
  echo "docker no encontrado"
fi

if docker compose version >/dev/null 2>&1; then
  docker compose version
else
  echo "docker compose no disponible"
fi

echo
echo "== Archivos de entorno esperados =="
for example in infra/airflow/.env.example infra/oracle/.env.example .env.example; do
  if [[ -f "$example" ]]; then
    echo "ok  $example"
  else
    echo "ERR falta $example"
    exit 1
  fi
done

echo
echo "== Limpieza basica =="
if git ls-files | grep -E '(__pycache__/|\.pyc$|logs/|volumes/|grafana\.db|\.zip$)' >/dev/null; then
  echo "ERR hay archivos generados versionados:"
  git ls-files | grep -E '(__pycache__/|\.pyc$|logs/|volumes/|grafana\.db|\.zip$)'
  exit 1
fi
echo "ok  sin caches, logs, volumenes o zips versionados"

echo
echo "== README principales =="
for readme in README.md docs/labs.md docs/runbooks/lab-operativa-diaria.md infra/airflow/README.md infra/oracle/README.md; do
  if [[ -f "$readme" ]]; then
    echo "ok  $readme"
  else
    echo "ERR falta $readme"
    exit 1
  fi
done

echo
echo "== Guias de instalacion =="
for guide in docs/install/README.md docs/install/cobertura.md docs/install/reponer-laboratorio-desde-cero.md docs/install/docker.md docs/install/visual-studio-code.md docs/install/airflow.md docs/install/postgresql.md docs/install/azurite.md docs/install/oracle.md docs/install/starship.md; do
  if [[ -f "$guide" ]]; then
    echo "ok  $guide"
  else
    echo "ERR falta $guide"
    exit 1
  fi
done

echo
echo "Chequeo completado."
