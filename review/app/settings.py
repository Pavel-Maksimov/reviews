import os

FLAMP_URL = 'http://ufa.flamp.ru/search/вкусно%20и%20точка'
# DATABASE = 'postgresql+psycopg2://scraping:12345@db:5432/scraping'
TIMEZONE = 5
DATABASE = {
    'drivername': 'postgresql+psycopg2',
    'host': os.environ.get('DB_HOST'),
    'port': os.environ.get('DB_PORT'),
    'username': os.environ.get('POSTGRES_USER'),
    'password': os.environ.get('POSTGRES_PASSWORD'),
    'database': os.environ.get('POSTGRES_DB')
}
