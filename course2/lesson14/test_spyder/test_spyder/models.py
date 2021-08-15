from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

#import settings


DeclarativeBase = declarative_base()


def db_connect():
    
    return create_engine('sqlite:///alembic_db.sql', echo=True)


def create_channel_table(engine):
    
    DeclarativeBase.metadata.create_all(engine)


class Channels(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "ytchannels"

    id = Column(Integer, primary_key=True)
    author = Column('author', String)
    quote = Column('quote', String)
    url = Column('url', String)
    tags = Column('tags', String)
    born_date = Column('born_date', String)
    born_location = Column('born_location', String)
    description = Column('description', String)
    