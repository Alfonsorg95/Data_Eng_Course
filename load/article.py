from sqlalchemy import Column, String, Integer
from base import Base

class Article(Base):

    __tablename__ = 'articles'

    uid = Column(String, primary_key=True)
    body = Column(String)
    title = Column(String)
    url = Column(String)
    newspaper_uid = Column(String)
    host = Column(String)
    title_words = Column(Integer)
    body_words = Column(Integer)

    def __init__(self, uid, body, title, url, newspaper_uid, host, title_words, body_words) -> None:
        self.uid = uid
        self.body = body
        self.title = title
        self.url = url
        self.newspaper_uid = newspaper_uid
        self.host = host
        self.title_words = title_words
        self.body_words = body_words