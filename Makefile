.PHONY: build up jupyter down

IMAGE := capability-lab:hc08
CONTAINER := capability-lab-jupyter
PORT := 8889

build:
	docker build -t $(IMAGE) .

up: build
	docker run --detach --rm --name $(CONTAINER) \
	  --publish 127.0.0.1:$(PORT):$(PORT) \
	  --mount "type=bind,source=$(CURDIR),target=/app" \
	  --workdir /app/notebooks $(IMAGE) \
	  jupyter lab --ip=0.0.0.0 --port=$(PORT) --no-browser --allow-root --ServerApp.root_dir=/app

jupyter:
	@docker container inspect $(CONTAINER) >/dev/null || { echo "Start Jupyter with make up." >&2; exit 1; }
	@for attempt in 1 2 3 4 5 6 7 8 9 10; do \
	  url=$$(docker logs $(CONTAINER) 2>&1 | awk -v prefix='http://127.0.0.1:$(PORT)/lab?token=' 'index($$NF, prefix) == 1 { print $$NF; exit }'); \
	  if [ -n "$$url" ]; then open "$$url"; exit $$?; fi; \
	  sleep 1; \
	done; \
	echo "Jupyter did not report a login URL. Check docker logs $(CONTAINER) locally." >&2; exit 1

down:
	docker stop $(CONTAINER)
