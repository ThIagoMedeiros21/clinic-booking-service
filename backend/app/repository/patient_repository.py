from app.models.patient_models import Patient
from sqlalchemy.orm import Session
from datetime import date

def create_patient(db: Session, user_id: int, dob: date, phone: str):
    patient = Patient(
        user_id = user_id,
        dob = dob,
        phone = phone
    )
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

def found_all(db: Session):
    return db.query(Patient).all()

def found_by_id(db: Session, id: int):
    return db.query(Patient).filter_by(id = id).first()

def update_patient(db: Session, id:int, phone: str):
    patient = db.query(Patient).filter_by(id = id).first()
    if not patient:
        return None
    
    patient.phone = phone
    db.commit()
    db.refresh(patient)
    return patient

def delete_patient(db: Session, id: int):
    patient = db.query(Patient).filter_by(id = id).first()
    if not patient:
        return None
    db.delete(patient)
    db.commit()
    return patient
