from sqlalchemy import Column, Integer, TIMESTAMP, String, ForeignKey
from database import Base

class Appointment(Base):
    __tablename__ = "appointment"
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    patient_id = Column(Integer, ForeignKey("patient.id"), nullable = False)
    medic_id = Column(Integer, ForeignKey("medic.id"), nullable = False)
    clinic_id = Column(Integer, ForeignKey("clinic.id"), nullable = False)
    start_time = Column(TIMESTAMP, nullable = False)
    end_time = Column(TIMESTAMP, nullable = False)
    status = Column(String, nullable = False)