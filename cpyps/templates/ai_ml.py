"""
AI/ML project template files.
Adds machine learning pipeline, data ingestion, training, evaluation, and notebook files.
"""

from .common import COMMON_FILES

AI_ML_FILES = COMMON_FILES + [
    "src/data/__init__.py",
    "src/data/data_ingestion.py",
    "src/data/data_transformation.py",
    "src/models/__init__.py",
    "src/models/model_trainer.py",
    "src/models/model_evaluation.py",
    "src/pipelines/__init__.py",
    "src/pipelines/training_pipeline.py",
    "src/pipelines/prediction_pipeline.py",
    "notebooks/",
    "notebooks/01_eda.ipynb",
    "notebooks/02_model_experimentation.ipynb",
    "artifacts/",
    "mlflow_config.yaml",
]
