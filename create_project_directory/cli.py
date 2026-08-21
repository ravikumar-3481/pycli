import os
import sys
import argparse
import time
from pathlib import Path
import logging
from rich.logging import RichHandler
from rich.console import Console

console = Console()

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(
        console=console,
        rich_tracebacks=True,
        show_time=True,
        show_path=False,
        markup=True
    )]
)

logger = logging.getLogger("project_setup")

LIST_OF_FILES = [
    ".github/workflows/.gitkeep",
    ".github/workflows/ci-cd.yml",
    ".github/workflows/deploy.yml",
    "data/raw/",
    "data/processed/",
    "data/source.md",
    "docs/architecture.md",
    "docs/setup.md",
    "docs/api.md",
    "docs/requirements/prd.md",
    "docs/requirements/trd.md",
    "docs/decisions/decision.md",
    "src/__init__.py",
    "src/core/__init__.py",
    "src/api/__init__.py",
    "src/features/__init__.py",
    "src/components/__init__.py",
    "src/utils/__init__.py",
    "src/config/__init__.py",
    "src/config/configuration.py",
    "src/pipeline/__init__.py",
    "src/entity/__init__.py",
    "src/constants/__init__.py",
    "src/cache/__init__.py",
    "research/",
    "templates/",
    "logs/",
    "config/config.yaml",
    "config/config.py",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    ".gitignore",
    "README.md",
    ".env",
    ".env.example",
]


def create_project_structure(project_name: str):
    root_dir = Path(project_name)

    if root_dir.exists() and any(root_dir.iterdir()):
        logger.warning(
            f"[yellow]{root_dir}[/yellow] already exists and is not empty — continuing inside it."
        )

    root_dir.mkdir(parents=True, exist_ok=True)
    os.chdir(root_dir)
    logger.info(f"Project root created: [bold cyan]{root_dir.resolve()}[/bold cyan]")

    for filepath_str in LIST_OF_FILES:
        time.sleep(0.05)

        if filepath_str.endswith("/"):
            dir_path = Path(filepath_str)
            os.makedirs(dir_path, exist_ok=True)
            logger.info(f"Creating directory: [cyan]{dir_path}[/cyan]")
            continue

        filepath = Path(filepath_str)
        filedir, filename = os.path.split(filepath)

        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logger.info(
                f"Creating directory: [cyan]{filedir}[/cyan] for the file: [bold]{filename}[/bold]"
            )

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, "w"):
                pass
            logger.info(f"Creating empty file: [green]{filepath}[/green]")
        else:
            logger.warning(f"[yellow]{filename}[/yellow] already exists — [dim]skipping[/dim]")

    logger.info(f"[bold green]Project '{project_name}' structure created successfully![/bold green]")


def main():
    parser = argparse.ArgumentParser(
        prog="create-project-directory",
        description="Scaffold a production-ready AI/ML project structure anywhere.",
    )
    parser.add_argument(
        "name",
        nargs="?",
        default=None,
        help="Project name (root folder). If omitted, you'll be prompted.",
    )
    args = parser.parse_args()

    project_name = args.name if args.name else input("Enter Project Name: ").strip()

    if not project_name:
        logger.error("Project name cannot be empty!")
        sys.exit(1)

    logger.info(f"Starting project setup for: [bold cyan]{project_name}[/bold cyan]")
    create_project_structure(project_name)


if __name__ == "__main__":
    main()