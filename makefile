# Makefile

IMAGE_NAME := fast-api
CONTAINER_NAME := fastApi_container
VOLUME_NAME := fastApi_volume
APP_PATH:= /path/to/project/


.PHONY: build run start stop clean

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -d -v $(APP_PATH):/app -p 8080:8080 --name $(CONTAINER_NAME) $(IMAGE_NAME)

start:
	docker start $(CONTAINER_NAME)

stop:
	docker stop $(CONTAINER_NAME)

clean:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true
	docker rmi $(IMAGE_NAME) || true
	docker volume rm $(VOLUME_NAME) || true
