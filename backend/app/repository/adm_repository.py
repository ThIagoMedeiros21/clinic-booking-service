from app.models.adm_models import Adm
from sqlalchemy.orm import Session

def create_adm(db: Session, user_id: int, clinic_id: int):
    adm = Adm(
        user_id=user_id,
        clinic_id=clinic_id
    )
    db.add(adm)
    db.commit()
    db.refresh(adm)
    return adm

def found_by_clinic(db: Session, clinic_id: int):
    return db.query(Adm).filter_by(clinic_id=clinic_id).all()

def delete_adm(db: Session, id: int):
    adm = db.query(Adm).filter_by(id=id).first()
    if not adm:
        return None
    db.delete(adm)
    db.commit()
    return adm