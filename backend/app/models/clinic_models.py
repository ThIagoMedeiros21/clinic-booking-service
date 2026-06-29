from sqlalchemy import Column, Integer, String, TIMESTAMP
from app.core.database import Base

class Clinic(Base):
    __tablename__ = "clinic"

    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(50), nullable = False)
    address = Column(String(255), nullable = False)
    phone = Column(String(14), nullable = False)
    created_at = Column(TIMESTAMP, nullable = False)