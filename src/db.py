from sqlalchemy import create_engine
from models.base import Base
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URL = "postgresql://mvlcfr:cafer12.@localhost/recipe_app?client_encoding=utf8"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Drop all tables
Base.metadata.drop_all(bind=engine)

# Recreate all tables
Base.metadata.create_all(bind=engine)

Session = sessionmaker(engine)
session = Session()
