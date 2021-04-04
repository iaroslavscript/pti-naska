PYTHON=python3

.PHONY: all build clean lint

all: test build

test:
	tox

build:
	$(PYTHON) -m build

clean:
	rm -rf build/ dist/ *.egg-info/
	find . -name "*.pyc" -type f -delete
	find . -name __pycache__ -delete

