# Makefile for HuntFlow Webhook Models Python project
.PHONY: help venv install lint black flake mypy isort check all clean

# Variables
PYTHON_CMD := python3.8
PDM_VERSION := 2.20.1
VENV_DIR := .venv

# Default target
help:
	@echo "HuntFlow Webhook Models - Development Commands"
	@echo ""
	@echo "Available commands:"
	@echo "  make venv        Create virtual environment with Python 3.8 (FIRST!)"
	@echo "  make install     Install project dependencies"
	@echo "  make black       Format code with black"
	@echo "  make lint        Run all linters"
	@echo "  make all         Install dependencies and run all checks"
	@echo "  make clean       Clean up"

# Создание venv с Python 3.8 и установка PDM
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

# Установка зависимостей
install: venv
	@echo "=== Installing dependencies ==="
	@# Используем бинарные пакеты для pydantic-core
	@PDM_NO_BINARY="pydantic-core" $(VENV_DIR)/bin/pdm sync || \
		echo "PDM failed, trying alternative..." && \
		$(VENV_DIR)/bin/pip install black flake8 mypy isort pydantic-core
	@echo "✓ Installation complete!"

# Code formatting
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

# Linting
flake: venv
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "📋 Running flake8 linting..."
	@$(VENV_DIR)/bin/pdm run flake8
	@echo "✅ flake8: Linting complete"

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

# Run all linters
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

# Complete setup
all: install lint
	@echo ""
	@echo "✨ PROJECT SETUP COMPLETE"
	@echo "Everything is installed and all checks are passing!"
	@echo ""

# Clean up
clean:
	@echo "🧹 Cleaning up..."
	@rm -rf $(VENV_DIR) __pycache__ .pytest_cache .mypy_cache
	@find . -name "*.pyc" -delete
	@echo "✓ Cleanup complete"