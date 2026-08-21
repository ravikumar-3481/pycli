# 📖 CLI Reference Manual

Complete reference guide for the **`mkproject`** (`create-project-directory`) command-line interface.

---

## 🛠️ Synopsis

```bash
mkproject [POSITIONAL_NAME] [-t TYPE] [-h]
```

or via python module:

```bash
python -m create_project_directory.cli [POSITIONAL_NAME] [-t TYPE] [-h]
```

---

## 📋 Arguments & Flags

### Positional Arguments

| Argument | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `name` | `string` | `None` | The target project directory name. If omitted, the CLI interactively prompts for a project name. |

---

### Options & Flags

| Flag | Short | Choices | Description |
| :--- | :--- | :--- | :--- |
| `--type` | `-t` | `default`, `ai_ml`, `rag_based`, `backend`, `data_science` | Specifies the project structure template. If omitted, triggers the interactive selection menu. |
| `--help` | `-h` | N/A | Displays the command help screen and exits. |

---

## 🎨 Interactive Mode

If `--type` is not specified when running `mkproject`, the CLI presents a colorized interactive prompt:

```text
Select Project Type:
  1. default - Default / Standard AI-ML Project Structure
  2. ai_ml - AI / ML Project (Data ingestion, training & prediction pipelines, models, notebooks)
  3. rag_based - RAG Based Project (Vector Store, Embeddings, Retrievers, Document Loaders, Prompts)
  4. backend - Backend API Project (FastAPI/Flask API routes, services, DB models, schemas, Docker)
  5. data_science - Data Science Project (EDA notebooks, visualizations, reports, data management)

Enter choice number or project type name [default: 1 (default)]: 
```

**Acceptable Inputs at Prompt**:
- Number index: `1`, `2`, `3`, `4`, `5`
- Template key string: `default`, `ai_ml`, `rag_based`, `backend`, `data_science`
- Empty input (pressing Enter defaults to `1` / `default`)

---

## 🪟 Windows PATH Helper Script (`fix-path.ps1`)

If running `mkproject` returns `mkproject : The term 'mkproject' is not recognized...` on Windows, Python's `Scripts` folder is not in your environment `PATH`.

Run the bundled PowerShell script:

```powershell
.\fix-path.ps1
```

### What `fix-path.ps1` Does:
1. Locates Python's user `Scripts` directory automatically.
2. Checks if `Scripts` is present in the `User` environment `PATH`.
3. Permanently appends `Scripts` to `User` `PATH` if missing.
4. Safe to run multiple times without duplicating entries.

> ⚠️ **Note:** Re-open your PowerShell terminal window after running `fix-path.ps1` to load the updated `PATH`.

---

## 🚥 Exit Codes

| Code | Meaning | Cause |
| :--- | :--- | :--- |
| `0` | Success | Project scaffolding completed without errors. |
| `1` | Error | Project name was left empty or invalid argument provided. |
| `2` | Argument Parsing Error | Unrecognized command flag or invalid `-t` choice passed. |
