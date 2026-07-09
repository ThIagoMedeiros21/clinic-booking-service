from app.models.clinic_medics_models import ClinicMedics
from sqlalchemy.orm import Session

def create_clinic_medic(db: Session, medic_id: int, clinic_id: int):
    clinic_medic = ClinicMedics(
        medic_id=medic_id,
        clinic_id=clinic_id
    )
    db.add(clinic_medic)
    db.commit()
    db.refresh(clinic_medic)
    return clinic_medic

def found_by_clinic(db: Session, clinic_id: int):
    return db.query(ClinicMedics).filter_by(clinic_id=clinic_id).all()

def delete_clinic_medic(db: Session, id: int):
    clinic_medic = db.query(ClinicMedics).filter_by(id=id).first()
    if not clinic_medic:
        return None
    db.delete(clinic_medic)
    db.commit()
    return clinic_medic