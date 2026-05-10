# Docker

Configuracion Docker compartida.

El `docker-compose.yml` principal esta en la raiz del repositorio y usa perfiles para activar servicios por area.

```powershell
docker compose --profile observability up -d
docker compose --profile rag up -d
docker compose --profile data up -d
```
