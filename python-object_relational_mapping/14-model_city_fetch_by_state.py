#!/usr/bin/python3
"""
Script to print all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_cities_by_state(username, password, database):
    """
    Connects to the MySQL server and prints all City
    objects grouped by state from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
    """
    try:
        # Connect to the MySQL server
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                username, password, database
            ),
            pool_pre_ping=True
        )
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query and print all City objects grouped by state
        cities = session.query(City, State).join(State).order_by(City.id).all()
        for city, state in cities:
            print("{}: ({}) {}".format(state.name, city.id, city.name))

        session.close()
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        fetch_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("""
        Usage: ./14-model_city_fetch_by_state.py <username> <password>
        <database>
        """)
