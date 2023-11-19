#!/usr/bin/python3
""" changes the name of a State object
from the database
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
    new_instance = session.query(State).filter_by(id=2).first()
    new_instance.name = 'New Mexico'
    session.commit()
