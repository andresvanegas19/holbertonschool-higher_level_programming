#!/usr/bin/python3
"""This script execute in env of sqlalchemy
    and execute"""


from sqlalchemy import (Column, Integer, String, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import Base

Base = declarative_base()


class City(Base):
    """This is for a structure to save in Tables and use
    ORM to manipulated them"""
    __tablename__ = 'cities'
    id = Column(
        'id',
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True)
    name = Column('name', String(128), nullable=False)
    # state_id = Column(
    #     'state_id',
    #     Integer,
    #     ForeignKey('states.id'),
    #     nullable=False)
    # # Relationships
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    # states = relationship("State", foreign_keys=id)
