#!/usr/bin/python3
"""Start link class to table in database"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./6-model_state.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}', pool_pre_ping=True)
    Base.metadata.create_all(engine)
