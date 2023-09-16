#!/usr/bin/python3
"""Creating state "California" with the City "San Francisco" from db"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    newSt = State(name='California')
    newCt = City(name='San Francisco')
    session.add(newSt)
    session.add(newCt)
    session.commit()
