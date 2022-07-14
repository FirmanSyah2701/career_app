from fastapi import Form
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

    @classmethod
    def as_form(
        cls, 
        student_parent_number: str = Form(),
        student_name: str = Form(),
        student_class: str = Form(),
        gender: str = Form(),
        school_id: str = Form(),
        major: str = Form(),
        cp_one: str = Form(),
        cp_two: str = Form(),
        ce_one: str = Form(),
        ce_two: str = Form(),
        mcd_one: str = Form(),
        mcd_two: str = Form(),
        mcd_three: str = Form(),
        wwi_one: str = Form(),
        wwi_two: str = Form(),
        wwi_three: str = Form(),
        wwi_four: str = Form(),
        wwi_five: str = Form(),
        pgw_one: str = Form(),
        pgw_two: str = Form(),
        pgw_three: str = Form(),
    ): 
        return cls(
            student_parent_number = student_parent_number,
            student_name = student_name,
            student_class = student_class,
            gender = gender,
            school_id = school_id,
            major = major,
            cp_one = cp_one,
            cp_two = cp_two,
            ce_one = ce_one,
            ce_two = ce_two,
            mcd_one = mcd_one,
            mcd_two = mcd_two,
            mcd_three = mcd_three,
            wwi_one = wwi_one,
            wwi_two = wwi_two,
            wwi_three = wwi_three,
            wwi_four = wwi_four,
            wwi_five = wwi_five,
            pgw_one = pgw_one,
            pgw_two = pgw_two,
            pgw_three = pgw_three,
        )