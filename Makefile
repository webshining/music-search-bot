LOCATIONS_PATH := ./data/locales

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