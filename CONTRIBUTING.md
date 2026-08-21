# 🤝 Contributing to `mkproject`

Thank you for considering contributing to **`mkproject`** (`create-project-directory`)! Contributions of any kind are welcome—bug reports, feature requests, documentation improvements, and new project templates.

---

## 🚀 Quick Links

- 🐛 [Report a Bug](https://github.com/ravikumar-3481/pycli/issues/new?template=bug_report.md)
- 💡 [Request a Feature](https://github.com/ravikumar-3481/pycli/issues/new?template=feature_request.md)
- 🏗️ [Architecture & Custom Templates Guide](docs/ARCHITECTURE.md)

---

## 🛠️ Local Development Environment Setup

### 1. Fork and Clone the Repository
```bash
git clone https://github.com/ravikumar-3481/pycli.git
cd pycli
```

### 2. Set Up a Virtual Environment
```bash
# On Linux / macOS:
python -m venv venv
source venv/bin/activate

# On Windows (PowerShell):
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install in Editable Mode with Developer Dependencies
```bash
pip install -e ".[dev]"
```

---

## 🧪 Testing Guidelines

Before submitting a Pull Request, verify that all project templates scaffold correctly without errors.

Run the test suite script:

```bash
python -c "
import subprocess, shutil
from pathlib import Path

test_dir = Path('temp_test_scaffold')
if test_dir.exists():
    shutil.rmtree(test_dir)
test_dir.mkdir()

templates = ['default', 'ai_ml', 'rag_based', 'backend', 'data_science']

for t in templates:
    target = test_dir / f'test_{t}'
    res = subprocess.run(['mkproject', str(target), '-t', t], capture_output=True, text=True)
    if res.returncode == 0:
        print(f'✅ Template {t}: Success')
    else:
        print(f'❌ Template {t}: Failed - {res.stderr}')

shutil.rmtree(test_dir)
"
```

---

## 🎨 Code Style & Standards

- **Formatting**: We use [`Black`](https://github.com/psf/black) for Python code formatting:
  ```bash
  black create_project_directory
  ```
- **Linting**: We follow PEP 8 conventions:
  ```bash
  flake8 create_project_directory
  ```

---

## 📋 Pull Request Checklist

Before submitting your PR:
- [ ] Code follows PEP 8 style standards and is formatted with `Black`.
- [ ] All project templates generate expected directories and files cleanly.
- [ ] New template flags are added to `docs/TEMPLATES.md` and `README.md`.
- [ ] Commit messages are clear and descriptive.
