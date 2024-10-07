build:
	docker build -t simple-web-server .
	
bash: build
	docker run -it --rm simple-web-server sh

run: build
	docker run --rm -p 8080:80 simple-web-server

