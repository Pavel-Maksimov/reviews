import os

TIMEZONE = 5
BOT_TOKEN = os.environ.get('BOT_TOKEN')
DATABASE = {
    'drivername': 'postgresql+psycopg2',
    'host': os.environ.get('DB_HOST'),
    'port': os.environ.get('DB_PORT'),
    'username': os.environ.get('POSTGRES_USER'),
    'password': os.environ.get('POSTGRES_PASSWORD'),
    'database': os.environ.get('POSTGRES_DB')
}
