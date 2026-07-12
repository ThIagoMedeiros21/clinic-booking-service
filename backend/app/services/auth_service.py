from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.core import security
from app.models.user_models import User, Role
from app.repository.user_repository import create_user

def register(db: Session, email: str, password: str, role: Role):
    found = db.query(User).filter_by(email=email).first()
    if found:
        raise HTTPException(status_code = 400, detail = "This email is already in use")
    hashed_password = security.hash_password(password)

    return create_user(db, email, hashed_password, role)

def login(db: Session, email: str, password: str):
    found = db.query(User).filter_by(email=email).first()
    if not found:
        raise HTTPException(status_code = 404, detail = "User not Found")
    
    verify = security.verify_password(password, found.password)
    if not verify:
       raise HTTPException(status_code = 401, detail = "Incorrect Password") 

    token = security.create_access_token({"sub": str(found.id), "role": found.role})
    return {"access_token": token, "token_type": "bearer"}
