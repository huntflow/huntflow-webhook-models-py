# Makefile for HuntFlow Webhook Models Python project
.PHONY: help venv install install-pdm install-pip lint black black-check flake flake8 mypy isort isort-check check all clean

PYTHON_CMD := python3.8
PDM_VERSION := 2.20.1
VENV_DIR := .venv

help:
	@echo "HuntFlow Webhook Models - Development Commands"
	@echo ""
	@echo "Available commands:"
	@echo "  make venv         Create virtual environment with Python 3.8"
	@echo "  make install      Install dependencies (tries PDM, falls back to pip)"
	@echo "  make install-pdm  Install via PDM only"
	@echo "  make install-pip  Install via pip only"
	@echo "  make black        Format code with black"
	@echo "  make black-check  Check code formatting (CI mode)"
	@echo "  make flake        Run flake8 linting"
	@echo "  make flake8       Alias for flake"
	@echo "  make mypy         Run mypy type checking"
	@echo "  make isort        Sort imports with isort"
	@echo "  make isort-check  Check import sorting (CI mode)"
	@echo "  make lint         Run all code quality checks"
	@echo "  make check        Alias for 'make lint'"
	@echo "  make all          Full setup and all checks"
	@echo "  make clean        Clean up temporary files"

venv:
	@echo "=== Creating virtual environment with Python 3.8 ==="
	@if [ -d "$(VENV_DIR)" ]; then \
		echo "✓ Virtual environment already exists"; \
	else \
		echo "Creating new .venv..."; \
		$(PYTHON_CMD) -m venv $(VENV_DIR); \
		echo "Installing PDM..."; \
		$(VENV_DIR)/bin/pip install --upgrade pip pdm==$(PDM_VERSION); \
		echo "✓ Virtual environment ready with Python: $$($(VENV_DIR)/bin/python --version)"; \
	fi

install: venv
	@echo "=== Installing dependencies ==="
	@echo "Trying PDM installation first..."
	@if PDM_NO_BINARY="pydantic-core" $(VENV_DIR)/bin/pdm sync 2>/dev/null; then \
		echo "✅ PDM installation successful"; \
	else \
		echo "⚠️  PDM failed, trying pip..."; \
		$(VENV_DIR)/bin/pip install black flake8 mypy isort pydantic-core 2>/dev/null && \
		echo "✅ Pip installation successful (fallback)" || \
		(echo "❌ Both installation methods failed" && exit 1); \
	fi
	@echo "✓ Installation complete!"

install-pdm: venv
	@echo "Installing dependencies via PDM..."
	@PDM_NO_BINARY="pydantic-core" $(VENV_DIR)/bin/pdm sync
	@echo "✓ PDM installation complete"

install-pip: venv
	@echo "Installing dependencies via pip..."
	@$(VENV_DIR)/bin/pip install black flake8 mypy isort pydantic-core
	@echo "✓ Pip installation complete"

black: venv
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "🔧 Running black code formatter..."
	@$(VENV_DIR)/bin/pdm run black .
	@echo "✅ black: Code formatting complete"

black-check: venv
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "🔍 Checking code formatting with black..."
	@$(VENV_DIR)/bin/pdm run black . --check
	@echo "✅ black-check: Code is properly formatted"

flake: venv
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "📋 Running flake8 linting..."
	@$(VENV_DIR)/bin/pdm run flake8
	@echo "✅ flake8: Linting complete"

flake8: flake

mypy: venv
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "🔍 Running mypy type checking..."
	@$(VENV_DIR)/bin/pdm run mypy .
	@echo "✅ mypy: Type checking complete"

isort: venv
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "📦 Sorting imports with isort..."
	@$(VENV_DIR)/bin/pdm run isort .
	@echo "✅ isort: Imports sorted"

isort-check: venv
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "🔍 Checking import sorting with isort..."
	@$(VENV_DIR)/bin/pdm run isort . --check
	@echo "✅ isort-check: Imports are properly sorted"

lint: venv
	@echo ""
	@echo "🚀 STARTING CODE QUALITY CHECKS"
	@echo "═══════════════════════════════════════════════════════════════════════════════"
	@$(MAKE) black
	@$(MAKE) flake
	@$(MAKE) mypy
	@$(MAKE) isort-check
	@echo "═══════════════════════════════════════════════════════════════════════════════"
	@echo "🎉 All checks passed! ✓"
	@echo ""

check: lint

all: install lint
	@echo ""
	@echo "✨ PROJECT SETUP COMPLETE"
	@echo "Everything is installed and all checks are passing!"
	@echo ""

clean:
	@echo "🧹 Cleaning up..."
	@rm -rf $(VENV_DIR) __pycache__ .pytest_cache .mypy_cache
	@find . -name "*.pyc" -delete
	@echo "✓ Cleanup complete"
