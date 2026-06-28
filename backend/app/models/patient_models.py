from sqlalchemy import Column, Integer, Date, String, ForeignKey
from database import Base

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key = True, autoincrement = True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable = False)
    dob = Column(Date, nullable = False)
    phone = Column(String(20), nullable = False)
