#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__" and len(sys.argv) == 4:
    # create the uri of database
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])

    # configure Session class with desired options
    Session = sessionmaker()

    # TODO: pool_pre_ping
    # feature will normally emit SQL equivalent to “SELECT 1” each time a
    # connection is checked out from the pool; if an error is raised that
    # is detected as a “disconnect” situation, the connection will be
    engine = create_engine(db_uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # associate it with our custom Session class
    Session.configure(bind=engine)

    # work with the session
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print('{}: {}'.format(state.id, state.name))
