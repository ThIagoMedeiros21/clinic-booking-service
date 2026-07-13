from app.models.user_models import Role
from app.core.security import hash_password
from app.repository import user_repository
from sqlalchemy.orm import Session
from fastapi import HTTPException


def found_by_id(db: Session, id: int):
    return user_repository.search_by_id(db, id)

def get_all_users(db: Session, current_user: dict):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Acesso negado")
    return user_repository.search_all_users(db)

def update_user(db: Session, id: int, email: str, password: str, role: Role):
    hashed_password = hash_password(password)
    user = user_repository.update_user(db, id, email, hashed_password, role)
    if not user:
        raise HTTPException(status_code=404, detail="User not Found")
    return user

def delete_user(db: Session, id: int):
    return user_repository.delete_user(db, id)