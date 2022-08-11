import os

FLAMP_URL = 'http://ufa.flamp.ru/search/вкусно%20и%20точка'
TIMEZONE = 5
DATABASE = {
    'drivername': 'postgresql+psycopg2',
    'host': os.environ.get('DB_HOST'),
    'port': os.environ.get('DB_PORT'),
    'username': os.environ.get('POSTGRES_USER'),
    'password': os.environ.get('POSTGRES_PASSWORD'),
    'database': os.environ.get('POSTGRES_DB')
}
