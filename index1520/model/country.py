

from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Country(Base):
    __tablename__ = "country"

    id = Column(String, primary_key=True, autoincrement=True)
    name = Column(String)
