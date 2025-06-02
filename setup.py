# setup.py

from database import Base, engine  # Correct import
from models.business import Business
from models.permit import Permit

print("Creating database tables...")

Base.metadata.create_all(engine)

print("All tables created successfully!")
