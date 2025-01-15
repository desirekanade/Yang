# app/crud.py
from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user: models.User, updates: schemas.UserUpdate):
    if updates.email:
        user.email = updates.email
    if updates.password:
        user.hashed_password = get_password_hash(updates.password)
    db.commit()
    db.refresh(user)
    return user

def create_login_history(db: Session, user_id: int, user_agent: str):
    login_entry = models.LoginHistory(user_id=user_id, user_agent=user_agent)
    db.add(login_entry)
    db.commit()
    db.refresh(login_entry)
    return login_entry

def get_login_history(db: Session, user_id: int):
    return db.query(models.LoginHistory).filter(models.LoginHistory.user_id == user_id).all()
