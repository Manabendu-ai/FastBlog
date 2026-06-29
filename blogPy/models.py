from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    author = Column(String(50))
    body = Column(Text)
    published = Column(Boolean)
    user_email = Column(String(50), ForeignKey('users.email'))

    owner = relationship('User', back_populates="blogs")

class User(Base):
    __tablename__ = "users"
    email = Column(String(50), primary_key=True, index=True)
    name = Column(String(50))
    password = Column(String(255))

    blogs = relationship('Blog', back_populates="owner")
