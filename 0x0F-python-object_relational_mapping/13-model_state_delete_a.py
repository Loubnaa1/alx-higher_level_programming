#!/usr/bin/python3
""" deletes all State objects with
a name from the database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session_tes = sessionmaker(bind=engine)
    session = session_tes()
    for instance in session.query(State).filter(State.name.like('%a%')):
        session.delete(instance)
    session.commit()
