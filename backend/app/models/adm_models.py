from sqlalchemy import Column, Integer, ForeignKey
from app.core.database import Base

class Adm(Base):
    __tablename__ = "adm"
    id = Column(Integer, primary_key = True, autoincrement = True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable = False)
    clinic_id = Column(Integer, ForeignKey("clinic.id"), nullable = False)

