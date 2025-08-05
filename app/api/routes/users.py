# app/api/routes/user.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db  
from app.db.models.user import User
from app.schemas.user import UserCreate
import hashlib

router = APIRouter()

@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed = hashlib.sha256(user.password.encode()).hexdigest()
    db_user = User(
        name=user.name,
        email=user.email,
        password_hash=hashed,
        is_driver=user.is_driver
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"id": db_user.id, "message": "User registered"}
