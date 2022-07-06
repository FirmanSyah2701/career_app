from model import Student
from database.mongo import database as db
import uuid

class StudentRepo():

    @staticmethod
    async def retrieve():
        _student = []
        collection = db.get_collection('student').find()
        async for student in collection:
            _student.append(student)
        return _student

    @staticmethod
    async def insert(student: Student):
        id = str(uuid.uuid4())
        
        _student = {
            "_id": id,
            "student_parent_number": student.student_parent_number,
            "student_name": student.student_name,
            "student_class": student.student_class,
            "major": student.major,
            "career": {
                "career_planning": {
                    "cp_one": student.cp_one,
                    "cp_two": student.cp_two
                },
                "career_exploration": {
                    "ce_one": student.ce_one,
                    "ce_two": student.ce_two
                },
                "make_career_decisions": {
                    "mcd_one": student.mcd_one,
                    "mcd_two": student.mcd_two,
                    "mcd_three": student.mcd_three
                },
                "world_of_work_information": {
                    "wwi_one": student.wwi_one,
                    "wwi_two": student.wwi_two,
                    "wwi_three": student.wwi_three,
                    "wwi_four": student.wwi_four,
                    "wwi_five": student.wwi_five
                },
                "prefered_group_work": {
                    "pgf_one": student.pgf_one,
                    "pgf_two": student.pgf_two,
                    "pgf_three": student.pgf_three
                },
            }
        }

        await db.get_collection('student').insert_one(_student)