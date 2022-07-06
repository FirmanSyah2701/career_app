from pydantic import BaseModel
from typing import Union, Optional


class Admin(BaseModel):
    id: str = None
    email: str
    password: str
    school_name: str

class CareerPlanning(BaseModel):
    cp_one: str
    cp_two: str

class CareerExploration(BaseModel):
    ce_one: str
    ce_two: str

class MakeCareerDecisions(BaseModel):
    mcd_one: str
    mcd_two: str
    mcd_three: str

class WorldWorkInformation(BaseModel):
    wwi_one: str
    wwi_two: str
    wwi_three: str
    wwi_four: str
    wwi_five: str

class PreferedGroupWork(BaseModel):
    pgf_one: str
    pgf_two: str
    pgf_three: str

class Career(BaseModel):
    career_planning: Union[CareerPlanning, None] = None
    career_exploration: Union[CareerExploration, None] = None
    make_career_decisions: Union[MakeCareerDecisions, None] = None
    world_of_work_information: Union[WorldWorkInformation, None] = None
    prefered_group_work: Union[PreferedGroupWork, None] = None

class Student(BaseModel):
    id: str = None
    student_parent_number: str
    student_name: str
    student_class: str
    school_id: str
    major: str
    career: Union[Career, None] = None

class TokenData(BaseModel):
    email: Optional[str] = None