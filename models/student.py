from pydantic import BaseModel

class Student(BaseModel):
    id: str = None
    student_parent_number: str
    student_name: str
    student_class: str
    gender: str
    school_id: str
    major: str
    cp_one: str
    cp_two: str
    ce_one: str
    ce_two: str
    mcd_one: str
    mcd_two: str
    mcd_three: str
    wwi_one: str
    wwi_two: str
    wwi_three: str
    wwi_four: str
    wwi_five: str
    pgw_one: str
    pgw_two: str
    pgw_three: str
    maturity_career: str = None