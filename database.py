from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base


DATABASE_URL= "sqlite:///permit_tracker.db"

engine=create_engine(DATABASE_URL,)
Session= sessionmaker(bind=engine)
session= Session()

Base= declarative_base()