#!/usr/bin/python3
"""A script that lists all State objects that
contain the letter a from the database"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True
                    )
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()

    states = session.query(State).filter(State.name.contains('a')).all()

    for state in states:
        print(f'{state.id}: {state.name}')

    session.close()
