from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import timedelta, datetime, timezone
import os
from fastapi import HTTPException
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    data_copy = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    data_copy.update({"exp": expire})
    return jwt.encode(data_copy, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
    try:
        decode = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decode
    except JWTError:
         raise HTTPException(status_code=401, detail="Token inválido ou expirado")
