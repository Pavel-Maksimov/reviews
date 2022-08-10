import datetime
from sqlalchemy import create_engine, text
from sqlalchemy.engine.url import URL

from .settings import DATABASE, TIMEZONE


def read_reviews():
    engine = create_engine('postgresql+psycopg2://postgres:12345@db:5432/scraping')
    conn = engine.connect()

    with open('review_tracker/last_visit.txt', 'r') as f:
        last_visit_str = f.read()
    last_visit = datetime.datetime.strptime(last_visit_str, '%Y-%m-%d %H:%M:%S.%f%z')
    t = text('SELECT * FROM review WHERE date>:last_visit')
    result = conn.execute(t, last_visit=last_visit)
    reviews = []
    for el in result.fetchall():
        reviews.append(
            {
                'link': el[1],
                'name': el[2],
                'date': str(el[3]),
                'score': el[4],
                'text': el[5]
            }
        )

    last_visit = datetime.datetime.now(
        tz=datetime.timezone(datetime.timedelta(hours=TIMEZONE))
    )
    with open('review_tracker/last_visit.txt', 'w') as f:
        f.write(str(last_visit))
    return reviews
