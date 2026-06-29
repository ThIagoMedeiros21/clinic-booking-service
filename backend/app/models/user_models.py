from sqlalchemy import Integer, String, TIMESTAMP, Column, Enum, func
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
    created_at = Column(TIMESTAMP, nullable = False, server_default = func.now())
    role = Column(Enum(Role, values_callable=lambda obj: [e.value for e in obj]), nullable = False)