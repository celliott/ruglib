# rugs docker-compose makefile

# ENV Variables
AUTH_USER ?= "admin"
AUTH_PASS ?= "zer0"
ENVS = AUTH_USER=$(AUTH_USER) \
				AUTH_PASS=$(AUTH_PASS)

# Container Names
LOGGER_CONTAINER = rugs_worker_logger
HTTP_CONTAINER = rugs_endpoint_http

.PHONY: up

validate :
	$(ENVS) docker-compose config

build : validate
	$(ENVS) docker-compose build

pull :
	$(ENVS) docker-compose pull

up : pull
	$(ENVS) docker-compose up -d

up_local :
	$(ENVS) docker-compose up -d --no-build

down :
	$(ENVS) docker-compose down

reset : down
	make up

tail_logger :
	docker logs -f $(LOGGER_CONTAINER)

restart_logger :
	docker restart $(LOGGER_CONTAINER)	

restart_http :
	docker restart $(HTTP_CONTAINER)

tail_http :
	docker logs -f $(HTTP_CONTAINER)
