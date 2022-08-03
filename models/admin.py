from typing import List
from pydantic import BaseModel, Field

class Admin(BaseModel):
    id: str = None
    email: str
    password: str
    name: str
    school_name: str = None
    level: str = None

class ShowAdmin(BaseModel):
    id: str = None
    name: str = None
    email: str = None
    school_name: str = None
    msg: List = []

class School(BaseModel):
    id: str = Field(alias='_id')
    school_name: str

    def __str__(self):
        return "%s %s" % (self.id, self.school_name)