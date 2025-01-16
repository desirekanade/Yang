from sqlalchemy.orm import Session
from app import models, schemas

# 学生相关操作
def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    student = get_student(db, student_id)
    if student is None:
        return False
    db.delete(student)
    db.commit()
    return True

# 组相关操作
def get_group(db: Session, group_id: int):
    return db.query(models.Group).filter(models.Group.id == group_id).first()

def get_groups(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Group).offset(skip).limit(limit).all()

def create_group(db: Session, group: schemas.GroupCreate):
    db_group = models.Group(name=group.name)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

def delete_group(db: Session, group_id: int):
    group = get_group(db, group_id)
    if group is None:
        return False
    db.delete(group)
    db.commit()
    return True

# 学生和组的关联操作
def add_student_to_group(db: Session, student_id: int, group_id: int):
    student = get_student(db, student_id)
    group = get_group(db, group_id)
    if not student or not group:
        return False
    group.students.append(student)
    db.commit()
    return True

def remove_student_from_group(db: Session, student_id: int, group_id: int):
    student = get_student(db, student_id)
    group = get_group(db, group_id)
    if not student or not group:
        return False
    group.students.remove(student)
    db.commit()
    return True

def transfer_student(db: Session, student_id: int, from_group_id: int, to_group_id: int):
    remove_student_from_group(db, student_id, from_group_id)
    add_student_to_group(db, student_id, to_group_id)
    return True

