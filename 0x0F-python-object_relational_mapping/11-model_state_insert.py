#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__" and len(sys.argv) == 5:
    # create the uri of database
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])

    Session = sessionmaker()
    engine = create_engine(db_uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session.configure(bind=engine)

    session = Session()
    states = session.query(State)\
        .filter(State.name == '{}'.format(sys.argv[4]))\
        .order_by(State.id)\
        .all()
    if states:
        for state in states:
            print('{}'.format(state.id))
    else:
        print('Not found')
    session.close()
