from time import sleep

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

from app.models import Review
from app.flamp_funcs import scrape_flamp
from app import settings


engine = create_engine('postgresql+psycopg2://postgres:12345@db:5432/scraping')
Session = sessionmaker(bind=engine)
session = Session()
newest_time = session.query(func.max(Review.date)).first()[0]
# while True:
flamp_data = scrape_flamp(
    url=settings.FLAMP_URL,
    last_visit_time=newest_time
)
for note in flamp_data:
    review = Review(
        link=note[0],
        name=note[1],
        date=note[2],
        score=note[3],
        text=note[4]
    )
    session.add(review)
session.commit()
    # sleep(60*60*24)
