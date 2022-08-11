from time import sleep
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from app.models import Base
from app.settings import DATABASE


sleep(5)
url = URL.create(**DATABASE)
engine = create_engine(url)
Base.metadata.create_all(engine)
