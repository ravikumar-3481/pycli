"""
Project template registry and helper functions.
"""

from .common import COMMON_FILES
from .ai_ml import AI_ML_FILES
from .rag_based import RAG_BASED_FILES
from .backend import BACKEND_FILES
from .data_science import DATA_SCIENCE_FILES

PROJECT_TEMPLATES = {
    "default": COMMON_FILES,
    "ai_ml": AI_ML_FILES,
    "rag_based": RAG_BASED_FILES,
    "backend": BACKEND_FILES,
    "data_science": DATA_SCIENCE_FILES,
}

PROJECT_DESCRIPTIONS = {
    "default": "Default / Standard AI-ML Project Structure",
    "ai_ml": "AI / ML Project (Data ingestion, training & prediction pipelines, models, notebooks)",
    "rag_based": "RAG Based Project (Vector Store, Embeddings, Retrievers, Document Loaders, Prompts)",
    "backend": "Backend API Project (FastAPI/Flask API routes, services, DB models, schemas, Docker)",
    "data_science": "Data Science Project (EDA notebooks, visualizations, reports, data management)",
}


def get_project_files(project_type: str = "default") -> list:
    """
    Returns the file list corresponding to the requested project_type.
    Falls back to 'default' if project_type is unknown.
    """
    return PROJECT_TEMPLATES.get(project_type.lower(), COMMON_FILES)
