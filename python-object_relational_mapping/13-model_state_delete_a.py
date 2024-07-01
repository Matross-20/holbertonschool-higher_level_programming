#!/usr/bin/python3
"""
Script to delete all State objects with a name
containing the letter 'a' from the database
hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a(username, password, database):
    """
    Connects to the MySQL server and deletes all State
    objects with a name containing the letter 'a'
    from the specified database.

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

        # Query and delete all State objects
        # containing the letter 'a' in their name
        states_with_a = session.query(State)\
                               .filter(State.name.like('%a%'))\
                               .all()
        for state in states_with_a:
            session.delete(state)
        session.commit()

        session.close()
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        delete_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("""
        Usage: ./13-model_state_delete_a.py <username> <password>
        <database>
        """)
