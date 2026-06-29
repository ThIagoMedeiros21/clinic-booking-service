from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey, Enum
from app.core.database import Base
import enum

class AppointmentStatus(enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"

class Appointment(Base):
    __tablename__ = "appointment"
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    patient_id = Column(Integer, ForeignKey("patient.id"), nullable = False)
    medic_id = Column(Integer, ForeignKey("medic.id"), nullable = False)
    clinic_id = Column(Integer, ForeignKey("clinic.id"), nullable = False)
    start_time = Column(TIMESTAMP, nullable = False)
    end_time = Column(TIMESTAMP, nullable = False)
    status = Column(Enum(AppointmentStatus, values_callable=lambda obj: [e.value for e in obj]), nullable = False)