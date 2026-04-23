PYTHON ?= python3
VENV ?= .venv
ACTIVATE = . $(VENV)/bin/activate

.PHONY: setup install test lint format ci clean

setup:
	@./scripts/bootstrap.sh

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e .[dev]

test:
	pytest -q

lint:
	$(PYTHON) -m compileall -q tonprobe tests
	ruff check tonprobe tests

format:
	ruff format tonprobe tests

ci: lint test

clean:
	rm -rf $(VENV) .pytest_cache .ruff_cache
