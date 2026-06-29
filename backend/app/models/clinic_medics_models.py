from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from app.core.database import Base

class ClinicMedics(Base):
    __tablename__ = "clinic_medics"

    id = Column(Integer, primary_key = True, autoincrement = True)
    medic_id = Column(Integer, ForeignKey("medic.id"), nullable = False)
    clinic_id = Column(Integer, ForeignKey("clinic.id"), nullable = False)
    __table_args__ = (UniqueConstraint("medic_id", "clinic_id"),)