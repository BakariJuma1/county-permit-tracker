# setup.py

from database import Base, engine  # Correct import
from models.business import Business
from models.permit import Permit
from models.user import User

print("Creating database tables...")

Base.metadata.create_all(engine)

print("All tables created successfully!")
