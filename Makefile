install:
	pip install -r requirements.txt

dev:
	pip install -r requirements-dev.txt

format:
	black .

lint:
	flake8 .

test:
	pytest -v

run:
	python3 main.py
