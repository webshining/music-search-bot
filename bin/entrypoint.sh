#!/bin/sh

pw_migrate migrate --database $(python get_database_url.py) --directory ./data/migrations
python main.py