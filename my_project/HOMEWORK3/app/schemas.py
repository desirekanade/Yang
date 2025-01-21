from pydantic import BaseModel
from typing import List, Optional

class GroupBase(BaseModel):
    name: str

class GroupCreate(GroupBase):
    pass

class Group(GroupBase):
    id: int
    students: List['Student'] = []

    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    name: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    groups: List[Group] = []

    class Config:
        orm_mode = True

from app.schemas import Student
Group.update_forward_refs()
