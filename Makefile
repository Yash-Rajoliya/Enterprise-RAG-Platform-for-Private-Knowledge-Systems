.PHONY: setup lint test run build up down format

setup:
	pip install -r requirements.txt
	npm install --prefix apps/web-client
	npm install --prefix apps/admin-dashboard

lint:
	ruff check .
	black --check .

format:
	black .
	ruff check . --fix

test:
	pytest tests/

run:
	uvicorn apps.api-server.app.main:app --reload

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down