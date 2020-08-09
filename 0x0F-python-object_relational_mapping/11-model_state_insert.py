#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

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
        new_state = State(name='Louisiana')
        session.add(new_state)
        session.commit()
        session.flush()
        num = new_state.id
        print(num)
    except exc.SQLAlchemyError as e:
        print(e)

    finally:
        session.close()
