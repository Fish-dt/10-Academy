.PHONY: install lint type-check test docker-test

install:
	curl -LsSf https://astral.sh/uv/install.sh | sh
	uv sync

lint:
	uv run ruff check . --fix

type-check:
	uv run pyright .

test:
	uv run pytest

docker-test:
	docker build -t project-chimera-audit -f Dockerfile .
	docker run --rm project-chimera-audit