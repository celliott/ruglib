# ruglib docker-compose makefile

include .env

.PHONY : up

validate :
	docker-compose config

build : validate
	docker-compose build

up :
	docker-compose up -d

down :
	docker-compose down

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
