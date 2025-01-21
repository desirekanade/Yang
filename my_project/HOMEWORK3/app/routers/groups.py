from fastapi import APIRouter

router = APIRouter(
    prefix="/groups",
    tags=["groups"],
)

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, models, schemas
from app.database import get_db

@router.post("/", response_model=schemas.Group)
def create_group(group: schemas.GroupCreate, db: Session = Depends(get_db)):
    return crud.create_group(db=db, group=group)

@router.post("/", response_model=schemas.Group)
def create_group(group: schemas.GroupCreate, db: Session = Depends(get_db)):
    return crud.create_group(db=db, group=group)

@router.get("/{group_id}", response_model=schemas.Group)
def read_group(group_id: int, db: Session = Depends(get_db)):
    db_group = crud.get_group(db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group

@router.delete("/{group_id}")
def delete_group(group_id: int, db: Session = Depends(get_db)):
    result = crud.delete_group(db, group_id=group_id)
    if not result:
        raise HTTPException(status_code=404, detail="Group not found")
    return {"detail": "Group deleted"}

@router.post("/{group_id}/students/{student_id}")
def add_student_to_group(group_id: int, student_id: int, db: Session = Depends(get_db)):
    result = crud.add_student_to_group(db, student_id, group_id)
    if not result:
        raise HTTPException(status_code=404, detail="Group or Student not found")
    return {"detail": "Student added to group"}

@router.delete("/{group_id}/students/{student_id}")
def remove_student_from_group(group_id: int, student_id: int, db: Session = Depends(get_db)):
    result = crud.remove_student_from_group(db, student_id, group_id)
    if not result:
        raise HTTPException(status_code=404, detail="Group or Student not found")
    return {"detail": "Student removed from group"}

@router.get("/{group_id}/students/", response_model=List[schemas.Student])
def get_students_in_group(group_id: int, db: Session = Depends(get_db)):
    db_group = crud.get_group(db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group.students
