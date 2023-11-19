#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa
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
    instance = session.query(State).first()
    if instance is None:
        print("Nothing")
    else:
        print(instance.id, instance.name, sep=": ")
