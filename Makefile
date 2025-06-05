.PHONY: test lint format installer

test:
pytest -q

lint:
ruff check .

format:
ruff format --check .

installer:
scripts/build_installer.sh
