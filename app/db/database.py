from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi_sqlalchemy import db
from typing import Generator
import os
import sqlalchemy

SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
metadata = sqlalchemy.MetaData()


def getDB() -> Generator:
    try:
        dbSession = SessionLocal()
        yield dbSession
    finally:
        dbSession.close()
