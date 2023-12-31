#!/usr/bin/python3
""" prints the State object
with the name passed as argument from the database
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
    instance = session.query(State).filter(State.name == (argv[4],))
    try:
        print(instance[0].id)
    except IndexError:
        print("Not found")
