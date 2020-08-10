#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy import exc
from sqlalchemy.engine.url import URL
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy import (Column, Integer, String, ForeignKey, create_engine)




Base = declarative_base(class_registry={"states": State, "cities": City})

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
    state_id = Column(
        'state_id',
        Integer,
        ForeignKey('states.id'),
        nullable=False)



class State(Base):
    """This is for a structure to save in Tables and use
    ORM to manipulated them"""
    __tablename__ = 'states'
    id = Column(
        'id',
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True)
    name = Column('name', String(128), nullable=False)
    cities = relationship('City', cascade="all, delete, delete-orphan")


if __name__ == "__main__" and len(sys.argv) == 4:
    # create the uri of database

    db_uri = {
        'drivername': 'mysql',
        'username': sys.argv[1],
        'password': sys.argv[2],
        'host': 'localhost',
        'port': 3306,
        'database': sys.argv[3]
    }

    Session = sessionmaker()
    engine = create_engine(URL(**db_uri), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session.configure(bind=engine)
    session = Session()

    try:
        new_state = State(name='California')
        new_city = City(name='San Francisco', state_id='California')
        new_state.cities.append(new_city)
        session.add(new_state)

        session.commit()
        session.flush()


    except exc.SQLAlchemyError as e:
        print(e)

    finally:
        session.close()
