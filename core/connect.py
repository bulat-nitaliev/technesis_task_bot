from sqlalchemy import create_engine
from sqlalchemy.orm import Session



engine = create_engine('sqlite:///database.db')

def get_db()->Session:      
    return  Session(engine)
