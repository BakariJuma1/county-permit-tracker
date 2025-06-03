
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import User
from database import Base

engine = create_engine("sqlite:///app.db")
Session = sessionmaker(bind=engine)
session = Session()

# clear existing users
session.query(User).delete()
session.commit()

# Create user
user = User(username='bakari', password='jma', role='admin')
session.add(user)
session.commit()

# Create inspector
inspector_one=User(username='isaac',password='1234',role="inspector")
session.add(inspector_one)
session.commit()

# create biz owner
biz_owner = User(username='ken',password='1234',role='owner')
session.add(biz_owner)
session.commit()

print("User,inspectorand owner created!")
