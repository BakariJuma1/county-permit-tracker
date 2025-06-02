from sqlalchemy import String,Column,Integer,ForeignKey,Date
from sqlalchemy.orm import relationship
from database import Base
import datetime

class Business(Base):
    __tablename__ = 'businesses'

    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    owner = Column(String,nullable=False)
    business_type = Column(String,nullable = False)
    location = Column(String,nullable=False)

    permits = relationship("permit",back_populates="business",cascade="al,delete-orphan")

    def __repr__(self):
        return(f"<Business(name={self.name},Owner={self.owner})>")
