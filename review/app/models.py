from sqlalchemy import (
    Column, DateTime, Integer, SmallInteger, String, Text)

from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Review(Base):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    link = Column(String(3000))
    name = Column(String(150))
    date = Column(DateTime(timezone=True))
    score = Column(SmallInteger())
    text = Column(Text)
