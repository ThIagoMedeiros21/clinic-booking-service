from sqlalchemy.orm import Session
from app.repository import clinic_repository
from app.repository import adm_repository
from fastapi import HTTPException

def create_clinic(db: Session, name: str, address: str, phone: str, current_user: dict):
    clinic = clinic_repository.create_clinic(db, name, address, phone)
    adm_repository.create_adm(db, int(current_user["sub"]), clinic.id)
    return clinic

def found_all_clinic(db: Session):
    return clinic_repository.found_all_clinic(db)

def found_by_id(db: Session, id: int):
    clinic = clinic_repository.found_by_id(db, id)
    if not clinic:
        raise HTTPException(status_code = 404, detail = "Clinic not Found")
    return clinic

def update_clinic(db: Session, id: int, name: str, address: str, phone: str, current_user: dict):
    admins = adm_repository.found_by_clinic(db, id)
    for i in admins:
        if i.user_id == int(current_user["sub"]):
            return clinic_repository.update_clinic(db, id, address, name, phone)
    raise HTTPException(status_code = 403, detail = "Can´t Acess")
    

def delete_clinic(db: Session, id: int, current_user: dict):
    admins = adm_repository.found_by_clinic(db, id)
    for i in admins:
        if i.user_id == int(current_user["sub"]):
            return clinic_repository.delete_clinic(db, id)
    raise HTTPException(status_code = 403, detail="Can't access")