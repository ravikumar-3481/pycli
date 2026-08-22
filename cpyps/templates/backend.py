"""
Backend API project template files.
Adds main application entry, controllers/routes, models, schemas, services, middlewares, tests, and Docker setup.
"""

from .common import COMMON_FILES

BACKEND_FILES = COMMON_FILES + [
    "src/main.py",
    "src/routes/__init__.py",
    "src/routes/api_v1.py",
    "src/controllers/__init__.py",
    "src/services/__init__.py",
    "src/services/base_service.py",
    "src/schemas/__init__.py",
    "src/schemas/request_response.py",
    "src/db/__init__.py",
    "src/db/session.py",
    "src/db/models.py",
    "src/middlewares/__init__.py",
    "src/middlewares/auth.py",
    "src/middlewares/cors.py",
    "tests/__init__.py",
    "tests/conftest.py",
    "tests/test_api.py",
    "Dockerfile",
    "docker-compose.yml",
]
