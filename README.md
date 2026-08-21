# mkproject

A simple CLI tool that scaffolds a complete AI/ML project folder structure with a single command — install it once, then run `mkproject` from any terminal, on any device.

## Features

- One-line project scaffolding — no more manually creating the same folders every time
- Works from any directory, on any machine, once installed
- Prompts for a project name if you don't pass one as an argument
- Lightweight — built with plain Python and `argparse`, no heavy dependencies

## Installation

### Option 1: Install directly from GitHub (recommended)

```bash
pip install git+https://github.com/ravikumar-3481/pycli.git
```



### Option 2: Install locally (for development/testing)

Clone the repo and install in editable mode:

```bash
git clone https://github.com/ravikumar-3481/pycli.git
cd pycli
pip install -e .
```

## Usage

Create a new project by passing a name directly:

```bash
mkproject "my-new-project"
```

Or run it without arguments and you'll be prompted for a name:

```bash
mkproject
```

This creates a new project folder in your current directory with a standard AI/ML project structure ready to go.

## Windows PATH Setup

On Windows, if `mkproject` isn't recognized after installing, it usually means Python's `Scripts` folder isn't on your PATH. This repo includes a helper script to fix that automatically:

```powershell
.\fix-path.ps1
```

This script:
- Detects your Python `Scripts` folder automatically
- Checks whether it's already in your PATH
- Adds it permanently to your User PATH if it's missing
- Is safe to re-run (idempotent)

**Important:** After running the script, close and reopen PowerShell for the PATH change to take effect.

## Project Structure

```
project-scaffolder/
├── .gitignore
├── README.md
├── fix-path.ps1
├── pyproject.toml
└── create_project_directory/
    ├── __init__.py
    └── cli.py
```

## Requirements

- Python 3.8+
- pip

## Contributing

Issues and pull requests are welcome. If you run into a bug or have an idea for an improvement, feel free to open an issue.

## License

MIT License — feel free to use, modify, and distribute.