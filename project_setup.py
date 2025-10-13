#!/usr/bin/env python3
"""
Enhanced project_setup.py

Sets up the SmartClimateForecast repository with advanced modules
for digital twin simulation, IoT data handling, monitoring,
and experiment tracking — designed for local-first AI/ML development.

Usage:
    python project_setup.py
"""

from pathlib import Path

# ---------------------------------------------------------------------
# 1. BASE STRUCTURE (your existing layout)
# ---------------------------------------------------------------------
STRUCTURE = {
    ".github/workflows": ["ci-cd.yml"],
    "app/static/css": ["style.css"],
    "app/static/images": ["ahfid_logo.png"],
    "app/static/js": ["script.js"],
    "app/templates": ["index.html", "prediction.html", "faq.html"],
    "artifacts": [".gitkeep"],
    "config": ["config.yaml", "params.yaml"],
    "data": [".gitkeep"],
    "logs": ["running_logs.log"],
    "notebooks": [
        "01_data_ingestion.ipynb",
        "02_prepare_base_model.ipynb",
        "03_model_training.ipynb",
        "04_model_evaluation.ipynb",
        "05_model_inference.ipynb",
    ],
    "notebooks/artifacts": [".gitkeep"],
    "src/SmartClimateForecast/components": [
        "__init__.py",
        "data_ingestion.py",
        "model_evaluation.py",
        "model_trainer.py",
        "prepare_base_model.py",
    ],
    "src/SmartClimateForecast/config": ["__init__.py", "configuration.py"],
    "src/SmartClimateForecast/entity": ["__init__.py", "config_entity.py"],
    "src/SmartClimateForecast/pipeline": [
        "__init__.py",
        "predict.py",
        "stage_01_data_ingestion.py",
        "stage_02_prepare_base_model.py",
        "stage_03_model_trainer.py",
        "stage_04_model_evaluation.py",
    ],
    "src/SmartClimateForecast/utils": ["__init__.py", "common.py", "logger.py"],
    "src/SmartClimateForecast/constants": ["__init__.py"],
    "tests": [
        "test_data_pipeline.py",
        "test_digital_twin.py",
        "test_model_training.py",
        "test_model_evaluation.py",
        "test_api_endpoints.py",
        "test_monitoring.py",
        "test_utils.py",
        "test_predict_pipeline.py",
        ],
}

# ---------------------------------------------------------------------
# 2. NEW MODULES (for advanced functionality)
# ---------------------------------------------------------------------
NEW_MODULES = {
    # --- Digital Twin Core ---
    "digital_twin": [
        "__init__.py",
        "state_manager.py",
        "model_coupling.py",
        "visualization.py",
        "scheduler.py",
        "README.md",
    ],
    # --- Data Pipeline ---
    "data_pipeline/ingestion": ["__init__.py", "iot_data_listener.py"],
    "data_pipeline/transformation": ["__init__.py", "preprocess.py"],
    "data_pipeline/storage": ["__init__.py", "data_lake_handler.py"],
    # --- API Layer ---
    "api/routes": [
        "__init__.py",
        "forecast.py",
        "sensors.py",
        "healthcheck.py",
    ],
    "api/utils": ["__init__.py", "security.py", "response_models.py"],
    # --- Monitoring & Observability ---
    "monitoring": [
        "__init__.py",
        "metrics_collector.py",
        "alerts.py",
        "README.md",
    ],
    "monitoring/dashboards": ["grafana_template.json"],
    # --- Experiments & Tracking ---
    "experiments": [
        "config_experiments.yaml",
        "README.md",
        "runs/.gitkeep",
        "logs/.gitkeep",
    ],
    # --- Scripts & Automation ---
    "scripts": [
        "start_local.sh",
        "run_tests.sh",
        "retrain_model.sh",
        "backup_artifacts.sh",
    ],
    # --- Environment Files ---
    "env": [".env.development", ".env.production", ".env.test"],
}

# ---------------------------------------------------------------------
# 3. CORE TEMPLATE FILES
# ---------------------------------------------------------------------
FASTAPI_MAIN = """from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="SmartClimateForecast")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/predict", response_class=HTMLResponse)
async def predict_page(request: Request):
    return templates.TemplateResponse("prediction.html", {"request": request})

@app.get("/faq", response_class=HTMLResponse)
async def faq(request: Request):
    return templates.TemplateResponse("faq.html", {"request": request})
"""

REQUIREMENTS = """fastapi
uvicorn
pandas
numpy
scikit-learn
jinja2
pyyaml
pytest
mlflow
prometheus-client
"""

DOCKERFILE = """FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
"""

CI_CD_YML = """name: CI/CD

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: pytest -q
"""

RENDER_YAML = """services:
  - type: web
    name: SmartClimateForecast
    env: python
    plan: free
    buildCommand: "pip install -r requirements.txt"
    startCommand: "uvicorn app.main:app --host 0.0.0.0 --port 8000"
"""

PYTEST_INI = """[pytest]
addopts = -v -s
testpaths = tests
python_files = test_*.py
"""

SETUP_PY = """from setuptools import setup, find_packages

setup(
    name='SmartClimateForecast',
    version='0.2.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'fastapi', 'uvicorn', 'pandas', 'numpy', 'scikit-learn', 'mlflow'
    ],
)
"""

MAIN_TRAINING = """from src.SmartClimateForecast.pipeline.stage_01_data_ingestion import *
from src.SmartClimateForecast.pipeline.stage_02_prepare_base_model import *
from src.SmartClimateForecast.pipeline.stage_03_model_trainer import *
from src.SmartClimateForecast.pipeline.stage_04_model_evaluation import *

if __name__ == "__main__":
    print("Running SmartClimateForecast training pipeline...")
"""

README_ADVANCED = """# SmartClimateForecast — Extended Modules Overview

## digital_twin/
Core simulation logic integrating AI models, physics-based models, and real-time sensor data.

## data_pipeline/
Handles IoT data ingestion, preprocessing, and data lake storage.

## api/
FastAPI routes for forecasts, sensors, and health checks.

## monitoring/
Includes Prometheus metrics and Grafana templates for live observability.

## experiments/
Experiment tracking and reproducibility setup using MLflow.

## scripts/
Automation tools for retraining, backups, and local testing.
"""

# ---------------------------------------------------------------------
# 4. WRITE HELPERS
# ---------------------------------------------------------------------
def write_file(path: Path, content: str = ""):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def main():
    base = Path.cwd()

    # Original structure
    for folder, files in STRUCTURE.items():
        for file in files:
            write_file(base / folder / file, "")

    # New advanced modules
    for folder, files in NEW_MODULES.items():
        for file in files:
            if file.endswith(".sh"):
                content = f"#!/usr/bin/env bash\necho 'Running {file}'"
                p = base / folder / file
                write_file(p, content)
                p.chmod(0o755)
            else:
                write_file(base / folder / file, "")

    # Core project files
    write_file(base / "app/main.py", FASTAPI_MAIN)
    write_file(base / "requirements.txt", REQUIREMENTS)
    write_file(base / "Dockerfile", DOCKERFILE)
    write_file(base / ".github/workflows/ci-cd.yml", CI_CD_YML)
    write_file(base / "render.yaml", RENDER_YAML)
    write_file(base / "pytest.ini", PYTEST_INI)
    write_file(base / "setup.py", SETUP_PY)
    write_file(base / "main.py", MAIN_TRAINING)
    write_file(base / "README.md", README_ADVANCED)

    print("✅ SmartClimateForecast project structure (extended version) created successfully!")


if __name__ == "__main__":
    main()