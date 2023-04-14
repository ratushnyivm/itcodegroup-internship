install:
	pip install -r requirements.txt

lint:
	python -m flake8 ./lesson_2/

test:
	python -m pytest
