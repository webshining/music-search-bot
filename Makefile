RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
LOCATIONS_PATH := ./data/locales
MIGRATIONS_PATH := ./data/migrations
DATABASE_URL := $(shell python get_database_url.py)

db_revision:
	pw_migrate create --auto --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH} ${RUN_ARGS}
	# pw_migrate create --auto --database $(python get_database_url.py) --directory ./data/migrations migrate
db_migrate:
	pw_migrate migrate --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH}
	# pw_migrate migrate --database $(python get_database_url.py) --directory ./data/migrations
db_rollback:
	pw_migrate rollback --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH} --count 1
	# pw_migrate rollback --database $(python get_database_url.py) --directory ./data/migrations --count 1
pybabel_extract:
	pybabel extract --input-dirs=. -o ${LOCATIONS_PATH}/bot.pot --project=bot
	# pybabel extract --input-dirs=. -o ./data/locales/bot.pot --project=bot
pybabel_init:
	pybabel init -i ${LOCATIONS_PATH}/bot.pot -d ${LOCATIONS_PATH} -D bot -l en
	# pybabel init -i ./data/locales/bot.pot -d ./data/locales -D bot -l en
	pybabel init -i ${LOCATIONS_PATH}/bot.pot -d ${LOCATIONS_PATH} -D bot -l ru
	# pybabel init -i ./data/locales/bot.pot -d ./data/locales -D bot -l ru
	pybabel init -i ${LOCATIONS_PATH}/bot.pot -d ${LOCATIONS_PATH} -D bot -l uk
	# pybabel init -i ./data/locales/bot.pot -d ./data/locales -D bot -l uk
pybabel_compile:
	# pybabel compile -d ./data/locales -D bot --statistics
	pybabel compile -d ${LOCATIONS_PATH} -D bot --statistics
pybabel_update:
	# pybabel update -i ./data/locales/bot.pot -d ./data/locales -D bot
	pybabel update -i ${LOCATIONS_PATH}/bot.pot -d ${LOCATIONS_PATH} -D bot