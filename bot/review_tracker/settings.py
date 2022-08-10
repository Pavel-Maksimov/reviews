import os

TIMEZONE = 5
BOT_TOKEN = '1769438523:AAFi6CpHk-Ys6Hc5kfABRHozlKRX1x28Jsc'
DATABASE = {
    'drivername': 'postgresql+psycopg2',
    'host': os.environ.get('DB_HOST'),
    'port': os.environ.get('DB_PORT'),
    'username': os.environ.get('POSTGRES_USER'),
    'password': os.environ.get('POSTGRES_PASSWORD'),
    'database': os.environ.get('POSTGRES_DB')
}
