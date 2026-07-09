from app.models.medic_models import Medic
from sqlalchemy.orm import Session

def create_medic(db: Session, user_id: int, crm: str,  speciality: str):
    medic = Medic(
        user_id = user_id,
        crm = crm, 
        speciality = speciality
    )
    db.add(medic)
    db.commit()
    db.refresh(medic)
    return medic

def found_all_medics(db: Session):
    return db.query(Medic).all()

def found_by_id(db: Session, id: int):
    return db.query(Medic).filter_by(id = id).first()

def update_medic(db: Session, id: int, crm: str, speciality: str):
    medic = db.query(Medic).filter_by(id = id).first()
    if not medic:
        return None
    
    medic.crm = crm
    medic.speciality = speciality
    db.commit()
    db.refresh(medic)
    return medic

def delete_medic(db: Session, id: int):
    medic = db.query(Medic).filter_by(id = id).first()
    if not medic:
        return None
    db.delete(medic)
    db.commit()
    return medic