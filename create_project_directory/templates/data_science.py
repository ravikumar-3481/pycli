"""
Data Science project template files.
Adds EDA notebooks, visualization helpers, data processing scripts, and report structures.
"""

from .common import COMMON_FILES

DATA_SCIENCE_FILES = COMMON_FILES + [
    "data/external/",
    "data/interim/",
    "notebooks/",
    "notebooks/01_eda.ipynb",
    "notebooks/02_feature_engineering.ipynb",
    "notebooks/03_modeling.ipynb",
    "reports/",
    "reports/figures/",
    "reports/summary_report.md",
    "src/data/make_dataset.py",
    "src/features/build_features.py",
    "src/visualization/__init__.py",
    "src/visualization/visualize.py",
]
