.PHONY: help dev run prod install deps clean

# ===== Variables =====
PYTHON   = .venv/Scripts/python.exe
UVICORN  = .venv/Scripts/uvicorn.exe
APP      = main:app
HOST     = 127.0.0.1
PORT     = 8000
WORKERS  = 4

# ===== Default target =====
help:
	@echo "FastAPI Learning - available commands:"
	@echo "  make dev       Start dev server with hot reload (default: 127.0.0.1:8000)"
	@echo "  make run       Start server without reload"
	@echo "  make prod      Start production server (0.0.0.0, 4 workers, no reload)"
	@echo "  make install   Install dependencies from requirements.txt"
	@echo "  make deps      Print current dependency versions"
	@echo "  make clean     Remove Python caches"

# ===== Run server =====
dev:
	$(UVICORN) $(APP) --reload --host $(HOST) --port $(PORT)

run:
	$(UVICORN) $(APP) --host $(HOST) --port $(PORT)

prod:
	$(UVICORN) $(APP) --host 0.0.0.0 --port $(PORT) --workers $(WORKERS)

# ===== Dependencies =====
install:
	$(PYTHON) -m pip install -r requirements.txt

deps:
	$(PYTHON) -m pip freeze

# ===== Cleanup =====
clean:
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null; true
	@rm -rf .pytest_cache .mypy_cache .ruff_cache 2>/dev/null; true
	@echo "Caches cleaned."
