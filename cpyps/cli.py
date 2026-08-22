import os
import sys
import argparse
import time
from pathlib import Path
import logging
from rich.logging import RichHandler
from rich.console import Console

try:
    from .templates import PROJECT_TEMPLATES, PROJECT_DESCRIPTIONS, get_project_files
except ImportError:
    # Fallback for running script directly
    from cpyps.templates import (
        PROJECT_TEMPLATES,
        PROJECT_DESCRIPTIONS,
        get_project_files,
    )

console = Console()

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[
        RichHandler(
            console=console,
            rich_tracebacks=True,
            show_time=True,
            show_path=False,
            markup=True,
        )
    ],
)

logger = logging.getLogger("project_setup")

# Default file structure list kept for backward compatibility and fallback
LIST_OF_FILES = PROJECT_TEMPLATES["default"]


def select_project_type_interactively() -> str:
    """Prompts the user to select a project type interactively."""
    console.print("\n[bold cyan]Select Project Type:[/bold cyan]")
    template_keys = list(PROJECT_TEMPLATES.keys())
    for index, key in enumerate(template_keys, start=1):
        desc = PROJECT_DESCRIPTIONS.get(key, "")
        console.print(f"  [bold green]{index}.[/bold green] [bold yellow]{key}[/bold yellow] - [dim]{desc}[/dim]")
    
    choice = input("\nEnter choice number or project type name [default: 1 (default)]: ").strip().lower()
    
    if not choice:
        return "default"
    
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(template_keys):
            return template_keys[idx]
    elif choice in PROJECT_TEMPLATES:
        return choice

    logger.warning(f"[yellow]Invalid selection '{choice}'. Falling back to default project type.[/yellow]")
    return "default"


def create_project_structure(project_name: str, file_list: list = None, project_type: str = "default"):
    if file_list is None:
        file_list = LIST_OF_FILES

    root_dir = Path(project_name)

    if root_dir.exists() and any(root_dir.iterdir()):
        logger.warning(
            f"[yellow]{root_dir}[/yellow] already exists and is not empty — continuing inside it."
        )

    root_dir.mkdir(parents=True, exist_ok=True)
    os.chdir(root_dir)
    logger.info(f"Project root created: [bold cyan]{root_dir.resolve()}[/bold cyan]")
    logger.info(f"Using project template: [bold yellow]{project_type}[/bold yellow]")

    for filepath_str in file_list:
        time.sleep(0.02)

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

    logger.info(f"[bold green]Project '{project_name}' ({project_type}) structure created successfully![/bold green]")


def main():
    parser = argparse.ArgumentParser(
        prog="create-project-directory",
        description="Scaffold a production-ready AI/ML, RAG, Backend, or Data Science project structure anywhere.",
    )
    parser.add_argument(
        "name",
        nargs="?",
        default=None,
        help="Project name (root folder). If omitted, you'll be prompted.",
    )
    parser.add_argument(
        "-t",
        "--type",
        choices=list(PROJECT_TEMPLATES.keys()),
        default=None,
        help="Type of project structure (default, ai_ml, rag_based, backend, data_science).",
    )
    args = parser.parse_args()

    project_name = args.name if args.name else input("Enter Project Name: ").strip()

    if not project_name:
        logger.error("Project name cannot be empty!")
        sys.exit(1)

    project_type = args.type if args.type else select_project_type_interactively()
    file_list = get_project_files(project_type)

    logger.info(f"Starting project setup for: [bold cyan]{project_name}[/bold cyan]")
    create_project_structure(project_name, file_list=file_list, project_type=project_type)


if __name__ == "__main__":
    main()
