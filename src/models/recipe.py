from .base import Base
from sqlalchemy import Column, ARRAY, String, ForeignKey
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.dialects.postgresql import UUID, JSON

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    author_id = Column(UUID(as_uuid=True), ForeignKey('authors.id'))
    ingredients = Column("ingredients", ARRAY(JSON))
    instructions = Column("instructions", ARRAY(String))