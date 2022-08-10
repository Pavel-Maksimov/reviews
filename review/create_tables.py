from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

from app.models import Base
from app.settings import DATABASE

engine = create_engine('postgresql+psycopg2://postgres:12345@db:5432/scraping')
Base.metadata.create_all(engine)
