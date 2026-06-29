from sqlalchemy import Integer, String, TIMESTAMP,Column, Enum
import enum
from app.core.database import Base

class Role(enum.Enum):
    admin = "admin"
    medic = "medic"
    patient = "patient"


class User(Base):
    __tablename__= "user"
    id = Column(Integer, primary_key = True, autoincrement = True)
    email = Column(String(255), nullable = False, unique = True)
    password = Column(String(255), nullable = False)
    created_at = Column(TIMESTAMP, nullable = False)
    role = Column(Enum(Role), nullable = False)