IMAGE_NAME = movies

.PHONY: build run

build:
	docker build -f dockerfile -t $(IMAGE_NAME) .

run:
	docker run -p 8080:8080 $(IMAGE_NAME)
