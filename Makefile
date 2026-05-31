SHELL := /bin/bash
PYTHON := $(shell command -v python3 2>/dev/null || command -v python 2>/dev/null)

.PHONY: status check test airflow-up airflow-down airflow-logs core-up core-down oracle-up oracle-down

status:
	git status --short --branch

check:
	bash scripts/check-lab.sh

test:
	$(PYTHON) -m unittest discover -s tests -p "test_*.py"

airflow-up:
	docker compose -f infra/airflow/docker-compose.yml up -d

airflow-down:
	docker compose -f infra/airflow/docker-compose.yml down

airflow-logs:
	docker compose -f infra/airflow/docker-compose.yml logs -f --tail=100

core-up:
	docker compose -f infra/core-stack/docker-compose.yml up -d

core-down:
	docker compose -f infra/core-stack/docker-compose.yml down

oracle-up:
	docker compose -f infra/oracle/docker-compose.yml up -d

oracle-down:
	docker compose -f infra/oracle/docker-compose.yml down
