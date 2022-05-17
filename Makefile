help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

activate: ## Activate virtual environment
	pip install pipenv==2022.4.8
	pipenv shell --python 3.7

install: ## Install requirements from pip
	pipenv install

dev-install: ## Install requirements from pip in dev environment
	pipenv install --dev

run: ## Run the service
	python -m app.service
