.PHONY: install add shell jupiter-server build run

help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install: ## Install dependences
	poetry install

add: ## add a package
	poetry add $(package)

shell: ## run poetry
	poetry shell

# poetry run jupiter notebook
jupyter-server: ## run jupiter notebook
	poetry run jupyter notebook --allow-root --ip=0.0.0.0 --port=8888

build: ## Build the Docker image
	docker build -t jupyter-server .
	

run: build ## Run the Docker container
	docker run -p 8888:8888 jupyter-server



	


	

	
