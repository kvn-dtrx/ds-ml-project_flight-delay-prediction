# ---
# title: Makefile for ds-ml-project_flight-delay-prediction
# ---

# ---

PYTHON_VERSION := 3.11.3
VENV := .venv

TARGETS := help unix win
.PHONY: $(TARGETS)

help: ## Displays available targets with description
	@bin/make-help.sh

unix: ## Set up virtual environment and dependencies on macOS/Linux
	pyenv local $(PYTHON_VERSION)
	python -m venv $(VENV)
	$(VENV)/bin/python -m pip install --upgrade pip
	$(VENV)/bin/python -m pip install -e .

win: ## Set up virtual environment and dependencies on Windows (PowerShell)
	pyenv local $(PYTHON_VERSION)
	python -m venv $(VENV)
	.\$(VENV)\Scripts\python.exe -m pip install --upgrade pip
	.\$(VENV)\Scripts\python.exe -m pip install -e .
