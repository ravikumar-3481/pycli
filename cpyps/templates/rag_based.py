"""
RAG (Retrieval-Augmented Generation) project template files.
Adds vector DB, embeddings, document loaders, chunkers, retrievers, prompt templates, and evaluation tools.
"""

from .common import COMMON_FILES

RAG_BASED_FILES = COMMON_FILES + [
    "data/documents/",
    "data/vector_store/",
    "src/vectordb/__init__.py",
    "src/vectordb/vector_store.py",
    "src/embeddings/__init__.py",
    "src/embeddings/embedder.py",
    "src/loaders/__init__.py",
    "src/loaders/document_loader.py",
    "src/text_splitter/__init__.py",
    "src/text_splitter/splitter.py",
    "src/retriever/__init__.py",
    "src/retriever/retrieval_chain.py",
    "src/prompts/__init__.py",
    "src/prompts/prompt_templates.py",
    "src/llm/__init__.py",
    "src/llm/llm_provider.py",
    "evals/__init__.py",
    "evals/rag_eval.py",
]
