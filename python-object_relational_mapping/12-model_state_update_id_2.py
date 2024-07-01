#!/usr/bin/python3
"""
Script to change the name of a State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state_name(username, password, database):
    """
    Connects to the MySQL server and changes the name
    of the State object with id = 2 to "New Mexico".

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

        # Query the State object with id = 2 and update its name
        state_to_update = session.query(State).filter_by(id=2).first()
        if state_to_update:
            state_to_update.name = "New Mexico"
            session.commit()

        session.close()
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        update_state_name(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("""
        Usage: ./12-model_state_update_id_2.py <username> <password>
        <database>
        """)
