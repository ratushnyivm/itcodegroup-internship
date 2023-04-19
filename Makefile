install:
	pip install -r requirements.txt

lint:
	python -m flake8

test:
	python -m pytest

venv:
	python -m venv venv
	source venv/bin/activate

setup: venv install
