# Variables
PYTHON=python
PIP=pip

install:
	$(PIP) install -r requirements.txt

format:
	black .
	isort .

lint:
	pylint api ml_pipeline tests

test:
	pytest

test-cov:
	pytest --cov=api --cov=ml_pipeline --cov=tests --cov-report=term-missing

docker-build:
	docker build -t ml-api .

docker-run:
	docker-compose up --build -d

docker-stop:
	docker-compose down

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +
	rm -rf .pytest_cache .mypy_cache coverage.xml htmlcov
