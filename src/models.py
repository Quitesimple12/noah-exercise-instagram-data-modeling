import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    userid = Column(Integer, primary_key=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    postid = Column(Integer, primary_key = True)
    postdesc = Column(String(1000), nullable=False)
    postpicid = Column(Integer, primary_key= True)
    userid = Column(Integer, ForeignKey('user.userid'))
    

    def to_dict(self):
        return {}

class Comment(Base):
    __tablename__ = 'comment'
    commentid = Column(Integer, primary_key=True)
    commenttext = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    postid = Column(Integer, ForeignKey('post.postid'))

class Follow(Base):
    __tablename__ = 'profile'
    followid = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey('user.userid'))
    isfollowed = Column(Boolean, default = False)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
