.PHONY: install add shell jupiter-server build run

help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

init: ## Init project
	poetry init --quiet --no-interaction

install: init ## Install dependences
	poetry install

add: ## add a package
	poetry add pandas
	poetry add notebook
	poetry add seaborn
	poetry add pydantic
	poetry add matplotlib

shell: ## run poetry
	poetry shell

# poetry run jupyter notebook --allow-root --ip=0.0.0.0 --port=8888
jupyter-server: install add ## run jupiter notebook
	poetry run jupiter notebook

jupyter: install run ## Run Jupyter notebook
	poetry run jupyter notebook

#build: ## Build the Docker image
#	docker build -t jupyter-server .
	

#run: build ## Run the Docker container
#	docker run -p 8888:8888 jupyter-server




# generate-csv: ## Generate CSV file
# 	poetry run python src/utils/files.py

# sample: ## Run sample
# 	poetry run python src/sample.py

# transform: ## Run transform
# 	poetry run python src/transform.py
	
