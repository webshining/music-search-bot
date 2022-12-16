DATABASE_URL := $(shell python _get_database_url.py)
MIGRATIONS_PATH := ./migrations
LOCALES_PATH := ./data/locales

run:
	python app.py
compose:
	docker-compose up -d $(service)
docker_logs: 
	docker-compose logs -f app
docker_rebuild: 
	docker-compose up -d --build --no-deps --force-recreate $(service)
pw_create:
	pw_migrate create --auto --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH} migrate
pw_migrate:
	pw_migrate migrate --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH}
pw_rollback:
	pw_migrate rollback --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH} --count 1
pybabel_extract: 
	pybabel extract --input-dirs=. -o $(LOCALES_PATH)/bot.pot
pybabel_init: 
	pybabel init -i $(LOCALES_PATH)/bot.pot -d $(LOCALES_PATH) -D bot -l en && \
	pybabel init -i $(LOCALES_PATH)/bot.pot -d $(LOCALES_PATH) -D bot -l ru && \
	pybabel init -i $(LOCALES_PATH)/bot.pot -d $(LOCALES_PATH) -D bot -l uk
pybabel_update: 
	pybabel update -i $(LOCALES_PATH)/bot.pot -d ./data/locales -D bot
pybabel_compile: 
	pybabel compile -d $(LOCALES_PATH) -D bot