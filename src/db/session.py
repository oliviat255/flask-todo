"""Create a database session using sqlalchemy"""
from sqlalchemy import create_engine # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore

engine = create_engine("sqlite:///db.sqlite")
Session = sessionmaker(bind=engine)
