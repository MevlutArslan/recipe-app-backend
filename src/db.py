from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URL = "postgresql://mvlcfr:cafer12.@localhost/recipe_app"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session = sessionmaker(engine)
session = Session()
