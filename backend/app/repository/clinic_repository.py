from app.models.clinic_models import Clinic
from sqlalchemy.orm import Session
from datetime import datetime, timezone

def create_clinic(db: Session, name: str, address: str, phone: str):
    clinic = Clinic(
        name = name,
        address = address,
        phone = phone, 
        created_at=datetime.now(timezone.utc)
    )
    db.add(clinic)
    db.commit()
    db.refresh(clinic)
    return clinic

def found_all_clinic(db: Session):
    return db.query(Clinic).all()

def found_by_id(db: Session, id: int):
    return db.query(Clinic).filter_by(id = id).first()

def update_clinic(db: Session, id: int, address: str, name: str, phone: str):
    clinic = db.query(Clinic).filter_by(id = id).first()
    if not clinic:
        return None
    clinic.address = address
    clinic.name = name
    clinic.phone = phone
    db.commit()
    db.refresh(clinic)
    return clinic


def delete_clinic(db: Session, id: int):
    clinic = db.query(Clinic).filter_by(id = id).first()
    if not clinic:
        return None
    db.delete(clinic)
    db.commit()
    return clinic