from .base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Author(Base):
    __tablename__ = 'authors'
    # id= Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, primary_key=True , unique=True)
    recipes = relationship("Recipe", backref="author")
