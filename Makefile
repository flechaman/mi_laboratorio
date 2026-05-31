SHELL := /bin/bash

.PHONY: status airflow-up airflow-down airflow-logs core-up core-down oracle-up oracle-down

status:
	git status --short --branch

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
