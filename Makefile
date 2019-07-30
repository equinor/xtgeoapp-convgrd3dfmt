xt.PHONY: clean

clean: clean-build clean-pyc clean-test  ## remove all Python build, test, coverage...


clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr wheel*/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +


clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +


clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr TMP/


dist: clean ## builds wheel package
	python setup.py bdist_wheel


install: dist ## version to VENV install place
	python -m pip install --upgrade .
