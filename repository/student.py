from models.student import Student
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
    async def retrieve_school_id(school_id: str):
        _student = []
        collection = db.get_collection('student').find({'school_id': school_id})
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
            "gender": student.gender,
            "school_id": student.school_id,
            "major": student.major,
            "cp_one": student.cp_one,
            "cp_two": student.cp_two,
            "ce_one": student.ce_one,
            "ce_two": student.ce_two,
            "mcd_one": student.mcd_one,
            "mcd_two": student.mcd_two,
            "mcd_three": student.mcd_three,
            "wwi_one": student.wwi_one,
            "wwi_two": student.wwi_two,
            "wwi_three": student.wwi_three,
            "wwi_four": student.wwi_four,
            "wwi_five": student.wwi_five,
            "pgw_one": student.pgw_one,
            "pgw_two": student.pgw_two,
            "pgw_three": student.pgw_three
        }

        await db.get_collection('student').insert_one(_student)
    
    @staticmethod
    async def destroy(id: str):
        return await db.get_collection('student').delete_one({"_id": id})

    @staticmethod
    async def destroy_all():
        return await db.get_collection('student').delete_many({})

