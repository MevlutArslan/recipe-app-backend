from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://mvlcfr:cafer12.@localhost/recipe_app"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

try:
    conn = engine.connect()
    print("Connection established successfully!")
    conn.close()
except OperationalError as e:
    print(f"The error '{e}' occurred.")