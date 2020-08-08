#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

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

    Session = sessionmaker(autoflush=True)
    engine = create_engine(URL(**db_uri), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session.configure(bind=engine)
    session = Session()

    try:
        session = Session()
        states = session.query(State)\
            .filter(State.name.like('%a%')) \
            .all()

        # for state in states:
        # states.delete()
        for state in states:
            session.delete(state)
            session.commit()

    except SQLAlchemyError as e:
        logger.error(e.args)
        session.rollback()

    finally:
        session.close()
