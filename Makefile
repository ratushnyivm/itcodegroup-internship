install:
	pip install -r requirements.txt

lint:
	python -m flake8 ./lesson_2/

test:
	python -m pytest

venv:
	python -m venv venv
	source venv/bin/activate

setup: venv install
