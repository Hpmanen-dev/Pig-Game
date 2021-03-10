#!/usr/bin/env make

PYTHON = py

.PHONY: pydoc

all:

install:
	$(PYTHON) -m pip install -r requirements.txt

installed:
	$(PYTHON) -m pip list

clean:
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf htmlcov
	rm -rf doc

clean-doc:
	rm -rf doc

unittest:
	 $(PYTHON) -m unittest discover Tests "*_test.py"

coverage:
	coverage run -m unittest discover Tests "*_test.py"
	coverage html
	coverage report -m

pylint:
	pylint *.py

flake8:
	flake8

pydoc:
	install -d doc/api
	pydoc -w $(PWD)
	mv *.html doc/api

pdoc:
	rm -rf doc/api
	pdoc --html -o doc/api .

doc: pdoc #pydoc sphinx

uml:
	install -d doc/uml
	pyreverse *.py
	dot -Tpng classes.dot -o doc/uml/classes.png
	dot -Tpng packages.dot -o doc/uml/packages.png
	rm -f classes.dot packages.dot
	ls -l doc/uml

lint: flake8 pylint

test: lint coverage
