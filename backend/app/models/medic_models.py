from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class Medic(Base):
    __tablename__ = "medic"
    id = Column(Integer, primary_key = True, autoincrement = True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable = False)
    crm = Column(String, nullable = False)
    speciality = Column(String, nullable = False)