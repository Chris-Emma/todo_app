from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#creating sqlite engine
engine = create_engine("sqlite:///database/todo.db")

#creating declarative_base instance
Base = declarative_base()

#creating session local for session maker
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

def init_db():
    Base.metadata.create_all(engine)

