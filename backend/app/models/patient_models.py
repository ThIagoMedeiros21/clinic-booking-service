from sqlalchemy import Column, Integer, Date, String, ForeignKey
from app.core.database import Base

class Patient(Base):
    __tablename__ = "patient"
    id = Column(Integer, primary_key = True, autoincrement = True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable = False)
    dob = Column(Date, nullable = False)
    phone = Column(String(20), nullable = False)
