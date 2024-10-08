command:=fastapi

build:
	docker build -t fastapi-app -f ops/api.Dockerfile .

	
bash: build
	docker run -it --rm fastapi-app sh
	docker run -t api -f ops/api.Dockerfiles


run: build
	docker run --rm -p 8000:80 fastapi-app 

local:
	docker run -it --rm -p 8000:8000 fastapi-app fastapi
	

build-api:
	docker build -t api -f ops/api.Dockerfile .

run-api: build-api
	#docker run --rm -p 8000:80 fastapi-app 
	#docker run -it --rm -p 8000:8000 fastapi-app fastapi
	docker run -it --rm -p 8080:8000 fastapi-app $(command)
