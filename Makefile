-include .env
export

dev.install:
	@poetry install

lint:
	@mypy service
	@flake8 service

run:
	@python -m frontend
