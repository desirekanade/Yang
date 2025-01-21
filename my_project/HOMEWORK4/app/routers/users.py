# app/routers/users.py
from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from app import schemas, models, crud
from app.database import get_db
from app.utils import verify_password, create_access_token, create_refresh_token, blacklist_token
from app.auth import get_current_user
from datetime import datetime

router = APIRouter()

@router.post("/register", response_model=schemas.User)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@router.post("/login", response_model=schemas.Token)
def login(user: schemas.UserCreate, request: Request, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    access_token = create_access_token(data={"sub": db_user.email})
    refresh_token = create_refresh_token(data={"sub": db_user.email})

    # 记录登录历史
    user_agent = request.headers.get('user-agent')
    crud.create_login_history(db=db, user_id=db_user.id, user_agent=user_agent)

    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@router.post("/refresh", response_model=schemas.Token)
def refresh_token(token: schemas.TokenRefresh):
    if is_token_blacklisted(token.refresh_token):
        raise HTTPException(status_code=401, detail="Refresh token has been revoked")
    try:
        payload = jwt.decode(token.refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    access_token = create_access_token(data={"sub": email})
    refresh_token = create_refresh_token(data={"sub": email})

    # 将旧的刷新令牌列入黑名单
    blacklist_token(token.refresh_token)

    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@router.put("/user/update", response_model=schemas.User)
def update_user(updates: schemas.UserUpdate, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    updated_user = crud.update_user(db=db, user=current_user, updates=updates)
    return updated_user

@router.get("/user/history", response_model=List[schemas.LoginHistory])
def get_history(current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    history = crud.get_login_history(db=db, user_id=current_user.id)
    return history

@router.post("/logout")
def logout(token: str = Depends(oauth2_scheme)):
    blacklist_token(token)
    return {"msg": "Successfully logged out"}
