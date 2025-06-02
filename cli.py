from database import session
from models.business import Business
from models.permit import Permit
from datetime import date, timedelta


def menu():
    while True:
        print