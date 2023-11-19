#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa
"""
from sys import argv

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session_tes = sessionmaker(bind=engine)
    session = session_tes()
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
