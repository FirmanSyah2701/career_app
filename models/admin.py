from fastapi import Form
from pydantic import BaseModel, Field

class Admin(BaseModel):
    id: str = None
    email: str
    password: str
    school_name: str = None
    level: str

class ShowAdmin(BaseModel):
    id: str = None
    email: str
    school_name: str

class School(BaseModel):
    id: str = Field(alias='_id')
    school_name: str

    def __str__(self):
        return "%s %s" % (self.id, self.school_name)