from app.repository import adm_repository
from sqlalchemy.orm import Session
from fastapi import HTTPException

def create_adm(db: Session, user_id: int, clinic_id: int, current_user: dict):
    admins = adm_repository.found_by_clinic(db, clinic_id)
    if not admins:
        return adm_repository.create_adm(db, user_id, clinic_id)
    for i in admins:
        if i.user_id == int(current_user["sub"]):
            return adm_repository.create_adm(db, user_id, clinic_id)
    raise HTTPException(status_code=403, detail="Can´t acess")

def delete_adm(db: Session, user_id: int, clinic_id: int, current_user: dict):
    admin = adm_repository.found_by_clinic(db, clinic_id)
    if not admin:
        raise HTTPException(status_code = 404, detail = "Not found")
    for i in admin:
        if i.user_id == int(current_user["sub"]):
            return adm_repository.delete_adm(db, user_id)
    raise HTTPException(status_code=403, detail="Can´t acess")

def found_by_clinic(db: Session, clinic_id: int, current_user: dict):
    admin = adm_repository.found_by_clinic(db, clinic_id)
    if not admin:
        raise HTTPException(status_code = 404, detail = "Not found")
    for i in admin:
        if i.user_id == int(current_user["sub"]):
            return adm_repository.found_by_clinic(db, clinic_id)
    raise HTTPException(status_code=403, detail="Can´t acess")