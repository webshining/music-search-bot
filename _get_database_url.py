from data.config import DIR, DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

database = f'sqlite:///{DIR}/data/database.sqlite3'
if DB_HOST and DB_NAME and DB_PASS and DB_USER and DB_PORT:
    database = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    

print(database)