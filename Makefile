.PHONY: all help qa clean coverage build docker-build run

# target: all - Default target. Does nothing.
all:
	@clear
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

# target: help - Display callable targets.
help:
	@clear
	@egrep "^# target:" [Mm]akefile

# target: qa - Run pytest
qa:
	pytest

# target: clean - delete pycache
clean:
	echo "### Cleaning *.pyc and .DS_Store files "
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '.DS_Store' -exec rm -f {} \;
	find . -name "__pycache__" -type d -exec rm -rf {} +

# target: coverage - Test coverage
coverage:
	py.test --cov=.

# target: build - Build pkg
build:
	python setup.py sdist

# target: setup-test - Test setup py
setup-test:
	python setup.py test

# target: docker-build - Build docker image with tag habrpars
docker-build:
	docker build . -t habrpars

# target: run in develop - Run main script (develop)
run:
	python3 habrpars/habrpars.py

# target: docker-test - Test code in docker
docker-test:
	docker run --rm habrpars python3 setup.py test
