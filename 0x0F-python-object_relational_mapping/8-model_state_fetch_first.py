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

    Session = sessionmaker()
    engine = create_engine(db_uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session.configure(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()
    if state:
        print('{}: {}'.format(state.id, state.name))
    else:
        print('Nothing')

    #  transactional state is rolled back as well.
    session.close()
