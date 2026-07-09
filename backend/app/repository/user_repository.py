from app.models.user_models import User, Role
from datetime import datetime, timezone
from sqlalchemy.orm import Session

def create_user(db: Session, email: str, password: str, role: Role):
    user = User(
        email=email,
        password=password,
        role=role,
        created_at=datetime.now(timezone.utc)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
    
def search_all_users(db: Session):
    return db.query(User).all()

def search_by_id(db: Session, id: int):
    return db.query(User).filter_by(id=id).first()

def update_user(db: Session, id: int, email: str, password: str, role: Role):
    user = db.query(User).filter_by(id = id).first()
    if not user:
        return None
    
    user.email = email
    user.password = password
    user.role = role
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, id: int):
    user = db.query(User).filter_by(id = id).first()
    if not user:
        return None

    db.delete(user)
    db.commit()
    return user