PYTHON ?= python3
VENV ?= .venv
VENV_PYTHON = $(VENV)/bin/python
VENV_PIP = $(VENV)/bin/pip
DOCKERHUB_USERNAME ?= kubaplociennik
DOCKERHUB_IMAGE ?= projekt-github-jakub
IMAGE_NAME = $(DOCKERHUB_USERNAME)/$(DOCKERHUB_IMAGE)

.PHONY: deps lint test run docker_build docker_push clean

deps:
	$(PYTHON) -m venv $(VENV)
	$(VENV_PYTHON) -m pip install --upgrade pip
	$(VENV_PIP) install -r requirements.txt

lint:
	$(VENV_PYTHON) -m flake8 app.py tests

test:
	$(VENV_PYTHON) -m unittest discover -s tests

run:
	$(VENV_PYTHON) -m flask --app app run --host 0.0.0.0 --port 5000

docker_build:
	docker build -t $(IMAGE_NAME):latest .

docker_push:
	docker push $(IMAGE_NAME):latest

clean:
	rm -rf $(VENV) __pycache__ tests/__pycache__

