# Makefile for managing pre-commit hooks

.PHONY: run-hooks

run-hooks:
	@echo "Running pre-commit hooks..."
	pre-commit run --all-files
