from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, Text
class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    author = Column(String(50))
    body = Column(Text)
    published = Column(Boolean)