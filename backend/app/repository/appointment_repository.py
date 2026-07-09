from app.models.appointment import Appointment, AppointmentStatus
from sqlalchemy.orm import Session
from datetime import datetime
def create_appointment(
        db: Session,
        patient_id: int,
        medic_id: int,
        clinic_id: int,
        start_time: datetime,
        end_time: datetime,
        status: AppointmentStatus
):
    appointment = Appointment(
        patient_id = patient_id,
        medic_id = medic_id,
        clinic_id = clinic_id,  
        start_time = start_time,
        end_time = end_time,
        status = status
    )
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment

def found_all_appointment(db: Session):
    return db.query(Appointment).all()

def found_by_id(db: Session, id: int):
    return db.query(Appointment).filter_by(id = id).first()

def update_appointment(db: Session, id: int, status: AppointmentStatus):
    appointment = db.query(Appointment).filter_by(id = id).first()
    if not appointment:
        return None
    
    appointment.status = status
    db.commit()
    db.refresh(appointment)
    return appointment

def delete_appointment(db: Session, id: int):
    appointment = db.query(Appointment).filter_by(id = id).first()
    if not appointment:
        return None
    db.delete(appointment)
    db.commit()
    return appointment