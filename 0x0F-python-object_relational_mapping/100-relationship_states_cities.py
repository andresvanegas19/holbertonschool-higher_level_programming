#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from sqlalchemy import exc

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
        new_city = City(name='San Francisco')
        session.add(new_state)
        session.add(new_city)

        session.commit()
        session.flush()


    except exc.SQLAlchemyError as e:
        print(e)

    finally:
        session.close()
