import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
SQLALCHEMY_DATABASE_URI = "postgresql://xzuismnj:a5PQ0RBUaVkZKhtVtz4hzWKH6X5osODI@mouse.db.elephantsql.com/xzuismnj"

engine = create_engine(SQLALCHEMY_DATABASE_URI,
                        connect_args={},
                        # echo_pool="debug",
                        ##asynchronous features
                        future= True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False , bind = engine)
Base = declarative_base()

#DB utilities
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    
