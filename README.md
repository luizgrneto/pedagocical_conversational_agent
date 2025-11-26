# Agente Conversacional Pedagógico

Este repositório contém código e notebooks para um agente conversacional pedagógico que utiliza vetores (vector store) e técnicas de recuperação de informações para responder perguntas baseadas em documentos.

## Conteúdo principal

- `scripts/` — scripts utilitários (por exemplo, `ingest.py`, `query.py`).
- `src/` — código-fonte do projeto, com subpastas para `config`, `loaders`, `pipelines`, `utils` e `vectorstore`.
- `data/` — dados e artefatos gerados (inclui um banco de dados Chroma em `data/db/`).
- `pca_agent_env/` — ambiente virtual Python (venv) usado para desenvolvimento.
- Notebooks:
  - `Agent_chromadb_llama3.ipynb` — notebook exploratório que integra ChromaDB e Llama-3 (exemplo de uso).
  - `Vector_Store.ipynb` — demonstrações e testes do armazenamento vetorial.

## Diretórios

pedagogical_conversational_agent/
│
├── src/
│   ├── __init__.py
│   │
│   ├── vectorstore/
│   │   ├── __init__.py
│   │   ├── hybrid_vector_store.py
│   │
│   ├── loaders/
│   │   ├── __init__.py
│   │   ├── pdf_loader.py
│   │   ├── txt_loader.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │
│   ├── pipelines/
│   │   ├── __init__.py
│   │   ├── ingest_pipeline.py
│   │   ├── query_pipeline.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── text_cleaning.py
│       └── logger.py
│   
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│
├── scripts/
│   ├── ingest.py
│   ├── query.py
│
├── tests/
│   ├── test_vector_store.py
│
├── requirements.txt
├── README.md
└── .gitignore

## Requisitos

- Python 3.10+
- Dependências listadas em `requirements.txt`.

## Instalação (rápida)

1. Clone o repositório:

   git clone <url-do-repositorio>

2. Crie e ative um ambiente virtual:

   python -m venv .venv
   .\.venv\Scripts\Activate.ps1  # PowerShell

3. Instale dependências:

   pip install -r requirements.txt


## Uso básico

- Ingestão de documentos para o vector store:

  python scripts\ingest.py

- Realizar consultas usando o vector store:

  python scripts\query.py

- Abrir e executar os notebooks (`Agent_chromadb_llama3.ipynb`, `Vector_Store.ipynb`) para exemplos interativos.