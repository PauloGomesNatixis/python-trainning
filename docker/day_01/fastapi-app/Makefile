build:
	docker build -t fastapi-app .
	
bash: build
	docker run -it --rm fastapi-app sh

run: build
	#docker run --rm -p 8000:80 fastapi-app 
	docker run -it --rm -p 8000:8000 fastapi-app fastapi

