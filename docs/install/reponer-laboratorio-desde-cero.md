# Reponer el laboratorio desde cero

## Objetivo

Reconstruir este laboratorio en un equipo nuevo o darselo a un compañero para que pueda montarlo sin depender de memoria, historico de terminal o configuraciones locales invisibles.

Esta guia es la ruta principal. Las guias especificas de `docs/install/` explican cada bloque con mas detalle.

## Resultado esperado

Al terminar deberias tener:

- WSL operativo en Windows 11.
- Git configurado con autenticacion SSH contra GitHub.
- Repo clonado y sincronizado.
- Docker y Docker Compose funcionando desde WSL.
- Python, entorno virtual y hooks basicos preparados.
- Prompt Starship opcional para ver rama y estado Git.
- Servicios principales arrancables con `make`.
- Checks del laboratorio pasando con `make check` y `make test`.

## 1. Preparar Windows 11 y WSL

Sigue la guia:

```text
docs/install/windows-wsl.md
```

Resumen:

```powershell
wsl --install
wsl --update
```

Dentro de WSL:

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y git curl tree make unzip ca-certificates
```

Verifica:

```bash
git --version
make --version
tree --version
```

## 2. Configurar GitHub por SSH

Sigue la guia:

```text
docs/install/git-github-ssh.md
```

Resumen:

```bash
ssh-keygen -t ed25519 -C "tu_email@example.com"
cat ~/.ssh/id_ed25519.pub
```

Pega la clave publica en GitHub:

```text
Settings -> SSH and GPG keys -> New SSH key
```

Verifica:

```bash
ssh -T git@github.com
```

## 3. Clonar el repositorio

Elige una carpeta de trabajo. En este laboratorio se usa:

```bash
mkdir -p /mnt/e/Github
cd /mnt/e/Github
git clone git@github.com:flechaman/mi_laboratorio.git
cd mi_laboratorio
```

Verifica:

```bash
git status --short --branch
git remote -v
```

El remoto debe usar SSH:

```text
git@github.com:flechaman/mi_laboratorio.git
```

## 4. Instalar Docker

Sigue la guia:

```text
docs/install/docker.md
```

Verifica desde WSL:

```bash
docker --version
docker compose version
docker ps
```

## 5. Preparar Python

Sigue la guia:

```text
docs/install/python.md
```

Resumen desde la raiz del repo:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Instala hooks:

```bash
pip install pre-commit
pre-commit install
```

## 6. Crear archivos locales de entorno

Los `.env` reales no viajan en Git. Se recrean desde plantillas.

```bash
cp .env.example .env
cp infra/airflow/.env.example infra/airflow/.env
cp infra/oracle/.env.example infra/oracle/.env
```

Para Core Stack crea `infra/core-stack/.env`:

```bash
nano infra/core-stack/.env
```

Contenido local de ejemplo:

```env
POSTGRES_USER=lab
POSTGRES_PASSWORD=lab
POSTGRES_DB=lab
GRAFANA_ADMIN_USER=admin
GRAFANA_ADMIN_PASSWORD=admin
```

Para `projects/azure_metrics_lab`:

```bash
cd projects/azure_metrics_lab
cp local.settings.azure.example.json local.settings.json
cd ../..
```

Edita `local.settings.json` con valores reales o de laboratorio.

## 7. Configurar prompt opcional

Sigue la guia:

```text
docs/install/starship.md
```

No es obligatorio, pero ayuda mucho a ver:

- Directorio actual.
- Rama Git.
- Archivos sin trackear.
- Commits pendientes de push.

## 8. Validar el laboratorio base

Desde la raiz del repo:

```bash
make check
make test
```

Resultado esperado:

```text
Chequeo completado.
Ran 5 tests
OK
```

## 9. Levantar servicios principales

Airflow:

```bash
make airflow-up
```

Accesos:

- Airflow: <http://localhost:8080>
- MinIO Console: <http://localhost:9001>

Core Stack:

```bash
make core-up
```

Acceso:

- Grafana: <http://localhost:3000>

Oracle:

```bash
make oracle-up
```

Puerto:

- Oracle: `localhost:1521`

Mock API:

```bash
docker compose -f projects/mock-api/docker-compose.yml up -d --build
```

Acceso:

- Swagger: <http://localhost:8001/docs>

## 10. Validar servicios

```bash
docker ps
make check
curl http://localhost:8001/health
```

Para ver logs:

```bash
make airflow-logs
docker logs lab-oracle --tail=100
docker logs mock-api --tail=100
```

## 11. Parar servicios

```bash
make airflow-down
make core-down
make oracle-down
docker compose -f projects/mock-api/docker-compose.yml down
```

## Que no se repone desde Git

Por seguridad y limpieza, estas cosas no se guardan en el repositorio:

| Elemento | Como se repone |
| --- | --- |
| `.env` reales | Copiar desde `.env.example` y rellenar valores. |
| `local.settings.json` | Copiar desde plantilla y rellenar valores. |
| Volumenes Docker | Se regeneran al arrancar servicios. |
| Logs | Se regeneran al ejecutar servicios. |
| Caches Python | Se regeneran automaticamente. |
| Datos reales o sensibles | Restaurar desde fuente segura externa. |
| Artefactos `*.zip` | Regenerar o compartir fuera de Git si son necesarios. |

## Checklist final para entregar a un compañero

- Tiene acceso al repo en GitHub.
- Tiene clave SSH configurada en GitHub.
- Tiene Docker Desktop funcionando con WSL.
- Ha clonado el repo por SSH.
- Ha creado los `.env` locales desde plantillas.
- Ejecuta `make check` correctamente.
- Ejecuta `make test` correctamente.
- Puede arrancar al menos un servicio, por ejemplo `make airflow-up` o Mock API.

## Orden recomendado de lectura

1. `docs/install/windows-wsl.md`
2. `docs/install/git-github-ssh.md`
3. `docs/install/docker.md`
4. `docs/install/python.md`
5. `docs/install/reponer-laboratorio-desde-cero.md`
6. Guias especificas del servicio que se quiera usar.
