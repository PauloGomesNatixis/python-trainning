init:
	poetry init -C app

add:
	poetry add fastapi uvicorn asyncpg python-decouple -C app

build-postgresql:
	docker build -t postgres ./postgres

build-app:
	docker build -t app ./app

build-all:
	docker build -t app ./app
	docker build -t postgres ./postgres

run-postgres:
	docker run -d --rm --name postgres --network app-network -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -p 5432:5432 postgres

run-app: build-all run-postgres
	docker run -it --rm --name app --network app-network -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_HOST=postgres -e POSTGRES_DB=postgres -v ${PWD}/app:/app -p 8000:8000 app poetry run uvicorn src.app:app --host 0.0.0.0 --port 8000


stop-all:
	docker stop app postgres