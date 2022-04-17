from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi_sqlalchemy import db
from typing import Generator

#SQLALCHEMY_DATABASE_URL = "postgresql://myuser:password@localhost/spotifiuby_database"
#
#engine = create_engine(
#    SQLALCHEMY_DATABASE_URL
#)
#
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def getDB() -> Generator:
    try:
        dbSession = db.session
        yield dbSession
    finally:
        dbSession.close()
