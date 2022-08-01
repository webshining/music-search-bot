from data.config import DB_PORT, DB_HOST, DB_PASS, DB_USER, DB_NAME

if DB_PORT and DB_HOST and DB_PASS and DB_USER and DB_NAME:
    database = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
else:
    database = 'sqlite:///data/database.sqlite'


print(database)
