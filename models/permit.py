from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import datetime


class Permit(Base):
    __tablename__='permits'

    id = Column(Integer,primary_key=True)
    permit_number = Column(String,unique=True,nullable=False)
    issue_date = Column(Date,nullable=False)
    expiry_date = Column(Date,nullable=False)

    business_id = Column(Integer,ForeignKey('businesses.id'))
    business = relationship('Business',back_populates='permits')

    @property
    def is_expired(self):
        return datetime.date.today() > self.expiry_date
    
    def __repr__(self):
        status = "Expired" if self.is_expired else "Active"
        return f"<Permit({self.permit_number},Status={status})>"

    