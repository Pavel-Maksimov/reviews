import datetime
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

from .settings import DATABASE


def read_reviews():
    """
    Check new records in database.
    Return dictionary representing fields of reviews.
    
    """
    url = URL.create(**DATABASE)
    engine = create_engine(url)
    conn = engine.connect()
    # получить дату последнего уже просмотренного отзыва
    with open('review_tracker/last_visit.txt', 'r') as f:
        last_visit_str = f.read()
    last_visit = datetime.datetime.strptime(last_visit_str, '%Y-%m-%d %H:%M:%S%z')
    t = text('SELECT * FROM review WHERE date>:last_visit')
    result = conn.execute(t, last_visit=last_visit)
    reviews = []
    data = result.fetchall()
    for el in data:
        reviews.append(
            {
                'ссылка': el[1],
                'имя пользователя': el[2],
                'дата': str(el[3]),
                'оценка': el[4],
                'текст': el[5]
            }
        )
    # сохранить дату последнего просмотренного отзыва, если имеется 
    if len(data) > 0:
        last_review = max(data, key=lambda x: x[3])
        with open('review_tracker/last_visit.txt', 'w') as f:
            f.write(str(last_review[3]))
    return reviews
