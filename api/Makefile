.PHONY: venv clean

VENV_NAME?=venv
PYTHON=$(VENV_NAME)/bin/python
PIP=$(VENV_NAME)/bin/pip

venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: requirements.txt
	python3 -m venv $(VENV_NAME)
	$(PIP) install -r requirements.txt

clean:
	rm -rf $(VENV_NAME)