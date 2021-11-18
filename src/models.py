import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Artifact(Base):
    __tablename__ = 'artifact'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    medium = Column (String(250))
    date = Column (String(250))
    dimensions = Column (String(250))
    classification = Column (String(250))
    # obligado poner datos si dice nullable=False
    dimensions = Column (String(250))
    department_id = Column (Integer, ForeignKey('department.id'))
    artist_id = Column (Integer, ForeignKey('artist.id'))
    artist = relationship ('Artist')
    department = relationship ('Department')

class Artist(Base):
    __tablename__ = 'artist'
    id = Column(Integer, primary_key=True)
    artist_name = Column(String(250))
    gender = Column(String(250))
    artist_display_bio = Column(String(250))
    artist_nationality = Column(String(250))
    department_id = Column (Integer, ForeignKey('department.id'))
    department = relationship ('Department')
   

class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    department_name_ = Column(String(250))

render_er(Base, 'diagram.png')