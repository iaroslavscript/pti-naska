PYTHON=python3

.PHONY: build clean

build:
	$(PYTHON) -m build

clean:
	rm -rf build/ dist/ ptinaska.egg-info/

