# RAG Local

Configuracion para pruebas de Retrieval Augmented Generation local.

Componentes sugeridos:

- Qdrant como vector store local.
- Modelos de embeddings locales o endpoint compatible con OpenAI.
- Documentos de prueba fuera de Git si contienen informacion sensible.

Levantar Qdrant:

```powershell
docker compose --profile rag up -d
```
