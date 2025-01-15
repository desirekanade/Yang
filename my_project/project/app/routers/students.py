from fastapi import APIRouter

router = APIRouter(
    prefix="/students",
    tags=["students"],
)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, models, schemas
from app.database import get_db

@router.post("/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)

@router.get("/", response_model=List[schemas.Student])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students

@router.get("/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    result = crud.delete_student(db, student_id=student_id)
    if not result:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": "Student deleted"}

@router.post("/{student_id}/transfer/")
def transfer_student(student_id: int, from_group_id: int, to_group_id: int, db: Session = Depends(get_db)):
    result = crud.transfer_student(db, student_id, from_group_id, to_group_id)
    if not result:
        raise HTTPException(status_code=400, detail="Transfer failed")
    return {"detail": "Student transferred"}
