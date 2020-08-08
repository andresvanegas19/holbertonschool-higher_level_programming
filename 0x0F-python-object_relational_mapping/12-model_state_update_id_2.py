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

    Session = sessionmaker()
    engine = create_engine(URL(**db_uri), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session.configure(bind=engine)
    session = Session()

    try:
        session = Session()
        state = session.query(State)\
            .filter(State.id == '2').first()

        state.name = 'New Mexico'
        session.commit()
        session.flush()

    except SQLAlchemyError as e:
        logger.error(e.args)
        session.rollback()

    finally:
        session.close()
