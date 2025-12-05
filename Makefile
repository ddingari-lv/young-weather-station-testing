.PHONY: setup run clean

PYTHON ?= python3

setup:
    $(PYTHON) -m venv venv
    . venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

run:
    . venv/bin/activate && $(PYTHON) src/main.py

clean:
    rm -rf venv