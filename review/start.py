from time import sleep
from datetime import datetime

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

from app.models import Review
from app.flamp_funcs import scrape_flamp
from app import settings


url = URL.create(**settings.DATABASE)
engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()
while True:
    # проверяем дату и время самого последнего записанного отзыва
    newest_time = session.query(func.max(Review.date)).first()[0]
    flamp_data = scrape_flamp(
        url=settings.FLAMP_URL,
        last_visit_time=newest_time
    )
    for note in flamp_data:
        review = Review(
            link=note['url'],
            name=note['name'],
            date=note['date'],
            score=note['score'],
            text=note['text']
        )
        session.add(review)
    session.commit()
    sleep(60*60*24)
