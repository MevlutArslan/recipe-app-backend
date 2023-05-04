from .base import Base
from sqlalchemy import Column, ARRAY, String, ForeignKey
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.dialects.postgresql import UUID, JSON

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    image_url = Column("imageUrl", String)
    author_name = Column(String, ForeignKey('authors.name'))
    recipe_yield = Column("yield", String)
    prepTime = Column("prepTime", String)
    cookTime = Column("cookTime", String)
    ingredients = Column("ingredients", ARRAY(JSON))
    instructions = Column("instructions", ARRAY(String))