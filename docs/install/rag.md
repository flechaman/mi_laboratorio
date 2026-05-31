# Instalacion: RAG local

## Objetivo

Preparar la base de laboratorios RAG local.

## Rutas

```text
infra/rag/
projects/ai-local-rag/
```

## Requisitos

- Python 3.
- Dependencias del proyecto cuando se definan.
- Modelo local, API externa o motor de embeddings segun el experimento.

## Preparacion inicial

```bash
cd projects/ai-local-rag
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Cuando exista `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Datos

No subas documentos privados, bases vectoriales generadas ni embeddings pesados.

Usa:

```text
data/raw/
data/processed/
```

solo para ejemplos pequenos y no sensibles.

## Notas

- Documenta el proveedor de embeddings o modelo local usado.
- Si se usa una API externa, define `.env.example` y deja secretos fuera de Git.
