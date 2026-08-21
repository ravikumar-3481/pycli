# 🚀 Quick Start Guide

Welcome to **`mkproject`** (`create-project-directory`). This guide will help you get up and running with project scaffolding in under 2 minutes.

---

## 📌 Prerequisites

- **Python 3.8+** installed on your system.
- **pip** package manager.

---

## ⚡ 1. Installation

Install `mkproject` globally using `pip`:

```bash
pip install git+https://github.com/ravikumar-3481/pycli.git
```

Verify the installation:
```bash
mkproject --help
```

---

## 🎯 2. Scaffolding Your First Project

### Method A: Interactive Selection (Recommended for Beginners)

Simply type `mkproject` in your terminal and press Enter. You will be prompted to enter your project name and choose a template:

```text
$ mkproject

Enter Project Name: my-ai-app

Select Project Type:
  1. default - Default / Standard AI-ML Project Structure
  2. ai_ml - AI / ML Project (Data ingestion, training & prediction pipelines, models, notebooks)
  3. rag_based - RAG Based Project (Vector Store, Embeddings, Retrievers, Document Loaders, Prompts)
  4. backend - Backend API Project (FastAPI/Flask API routes, services, DB models, schemas, Docker)
  5. data_science - Data Science Project (EDA notebooks, visualizations, reports, data management)

Enter choice number or project type name [default: 1 (default)]: 3
```

---

### Method B: Direct Command with Template Flag (`-t` / `--type`)

If you already know which project template you want, pass the `-t` or `--type` flag:

```bash
# 🤖 AI / Machine Learning Pipeline
mkproject churn_prediction_model -t ai_ml

# 🔍 RAG (Retrieval-Augmented Generation) App
mkproject enterprise_knowledge_rag -t rag_based

# 🌐 Backend REST API Service
mkproject payment_gateway_api -t backend

# 📊 Data Science & EDA Exploration
mkproject customer_insights_eda -t data_science
```

---

## 🛠️ 3. Post-Scaffolding Workflow

Once `mkproject` generates your project structure, follow these standard setup steps:

### Step 3.1: Navigate into your new project
```bash
cd my-ai-app
```

### Step 3.2: Create and activate a Python virtual environment
```bash
# On Linux / macOS:
python -m venv venv
source venv/bin/activate

# On Windows (PowerShell):
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Step 3.3: Install dependencies
Edit `requirements.txt` to include your domain dependencies (e.g. `torch`, `langchain`, `fastapi`, `pandas`), then run:
```bash
pip install -r requirements.txt
```

### Step 3.4: Configure Environment Variables
Copy `.env.example` to `.env` and fill in any required credentials:
```bash
cp .env.example .env
```

---

## 📚 Next Steps

- Explore [docs/TEMPLATES.md](TEMPLATES.md) to understand what files were created for your chosen template.
- Read [docs/CLI_REFERENCE.md](CLI_REFERENCE.md) for full CLI parameter options.
- Read [docs/ARCHITECTURE.md](ARCHITECTURE.md) if you want to create your own custom template!
