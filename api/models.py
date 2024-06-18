from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types.choice import ChoiceType
from datetime import datetime
from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=True)
    last_name = Column(String(30), nullable=True)
    email = Column(Text, nullable=True)
    username = Column(String(30), unique=True, nullable=True)
    password = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return self.username

    # Relationships
    blogs = relationship('Blog', back_populates='author')
    clientcomments = relationship('ClientComment', back_populates='client')


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    image = Column(String(255))
    name = Column(String(30), nullable=True)
    description = Column(Text, nullable=False)
    price = Column(Integer)
    price_type = Column(String(4))
    slug = Column(String(100), unique=True, nullable=True)
    count = Column(Integer)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return self.name


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))
    slug = Column(String(100), unique=True, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    # Relationship to user
    author = relationship('User', back_populates='blogs')


class ClientComment(Base):
    __tablename__ = 'clientcomments'

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    client_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationship to user
    client = relationship('User', back_populates='clientcomments')