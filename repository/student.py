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
    async def insert_seed():
        _student = [
            {
                "_id": str(uuid.uuid4()),
                "student_parent_number": "12345",
                "student_name": "Allan Predovic",
                "student_class": "12",
                "gender": "laki-laki",
                "school_id": "6c2d532c-b9e0-4031-9f39-32fc98caa745",
                "major": "TI",
                "cp_one": "S",
                "cp_two": "TS",
                "ce_one": "STS",
                "ce_two": "SS",
                "mcd_one": "STS",
                "mcd_two": "TS",
                "mcd_three": "TS",
                "wwi_one": "TS",
                "wwi_two": "SS",
                "wwi_three": "S",
                "wwi_four": "TS",
                "wwi_five": "TS",
                "pgw_one": "TS",
                "pgw_two": "STS",
                "pgw_three": "SS",   
                "maturity_career": ""
            },
            {
                "_id": str(uuid.uuid4()),
                "student_parent_number": "23456",
                "student_name": "Aurelie Quitzon",
                "student_class": "11",
                "gender": "perempuan",
                "school_id": "6c2d532c-b9e0-4031-9f39-32fc98caa745",
                "major": "TI",
                "cp_one": "STS",
                "cp_two": "TS",
                "ce_one": "TS",
                "ce_two": "SS",
                "mcd_one": "STS",
                "mcd_two": "TS",
                "mcd_three": "SS",
                "wwi_one": "S",
                "wwi_two": "STS",
                "wwi_three": "S",
                "wwi_four": "TS",
                "wwi_five": "STS",
                "pgw_one": "TS",
                "pgw_two": "S",
                "pgw_three": "SS",
                "maturity_career": ""
            },
            {
                "_id": str(uuid.uuid4()),
                "student_parent_number": "34567",
                "student_name": "Tess Haag",
                "student_class": "12",
                "gender": "perempuan",
                "school_id": "6c2d532c-b9e0-4031-9f39-32fc98caa745",
                "major": "TI",  
                "cp_one": "TS",
                "cp_two": "S",
                "ce_one": "SS",
                "ce_two": "S",
                "mcd_one": "SS",
                "mcd_two": "TS",
                "mcd_three": "S", 
                "wwi_one": "TS",
                "wwi_two": "TS",
                "wwi_three": "SS",
                "wwi_four": "SS",
                "wwi_five": "S",
                "pgw_one": "TS",
                "pgw_two": "STS",
                "pgw_three": "SS",
                "maturity_career": ""
            },
            {
                "_id": str(uuid.uuid4()),
                "student_parent_number": "34567",
                "student_name": "Katelynn Nolan",
                "student_class": "11",
                "gender": "perempuan",
                "school_id": "6c2d532c-b9e0-4031-9f39-32fc98caa745",
                "major": "TM",
                "cp_one": "TS",
                "cp_two": "S",
                "ce_one": "S",
                "ce_two": "STS",
                "mcd_one": "TS",
                "mcd_two": "SS",
                "mcd_three": "S",
                "wwi_one": "SS",
                "wwi_two": "SS",
                "wwi_three": "S",
                "wwi_four": "S",
                "wwi_five": "SS",
                "pgw_one": "SS",
                "pgw_two": "STS",
                "pgw_three": "TS",
                "maturity_career": ""
            },
            {
                "_id": str(uuid.uuid4()),
                "student_parent_number": "45678",
                "student_name": "Katelynn Nolan",
                "student_class": "11",
                "gender": "perempuan",
                "school_id": "6c2d532c-b9e0-4031-9f39-32fc98caa745",
                "major": "TM",
                "cp_one": "TS",
                "cp_two": "S",
                "ce_one": "S",
                "ce_two": "STS",
                "mcd_one": "TS",
                "mcd_two": "SS",
                "mcd_three": "S",
                "wwi_one": "SS",
                "wwi_two": "SS",
                "wwi_three": "S",
                "wwi_four": "S",
                "wwi_five": "SS",
                "pgw_one": "SS",
                "pgw_two": "STS",
                "pgw_three": "TS",  
                "maturity_career": ""
            },
            {
                "_id": str(uuid.uuid4()),
                "student_parent_number": "56789",
                "student_name": "Kasey King",
                "student_class": "11",
                "gender": "laki-laki",
                "school_id": "6c2d532c-b9e0-4031-9f39-32fc98caa745",
                "major": "TM",
                "cp_one": "SS",
                "cp_two": "S",
                "ce_one": "SS",
                "ce_two": "SS",
                "mcd_one": "S",
                "mcd_two": "STS",
                "mcd_three": "S",
                "wwi_one": "SS",
                "wwi_two": "STS",
                "wwi_three": "SS",
                "wwi_four": "STS",
                "wwi_five": "SS",
                "pgw_one": "S",
                "pgw_two": "SS",
                "pgw_three": "S",
                "maturity_career": ""
            },
            {
                "_id": str(uuid.uuid4()),
                "student_parent_number": "67890",
                "student_name": "Mathilde Mertz",
                "student_class": "11",
                "gender": "perempuan",
                "school_id": "6c2d532c-b9e0-4031-9f39-32fc98caa745",
                "major": "TP",
                "cp_one": "SS",
                "cp_two": "S",
                "ce_one": "S",
                "ce_two": "S",
                "mcd_one": "SS",
                "mcd_two": "S",
                "mcd_three": "TS",
                "wwi_one": "SS",
                "wwi_two": "TS",
                "wwi_three": "STS",
                "wwi_four": "TS",
                "wwi_five": "S",
                "pgw_one": "SS",
                "pgw_two": "SS",
                "pgw_three": "STS",  
                "maturity_career": ""            
            },
            {
                "_id": str(uuid.uuid4()),
                "student_parent_number": "78901",
                "student_name": "Connor Weissnat MD",
                "student_class": "10",
                "gender": "Laki-laki",
                "school_id": "6c2d532c-b9e0-4031-9f39-32fc98caa745",
                "major": "TP",    
                "cp_one": "SS",
                "cp_two": "S",
                "ce_one": "SS",
                "ce_two": "S",
                "mcd_one": "SS",
                "mcd_two": "TS",
                "mcd_three": "STS",
                "wwi_one": "SS",
                "wwi_two": "TS",
                "wwi_three": "STS",
                "wwi_four": "S",
                "wwi_five": "S",
                "pgw_one": "S",
                "pgw_two": "SS",
                "pgw_three": "SS",
                "maturity_career": ""
            },
            {
                "_id": str(uuid.uuid4()),
                "student_parent_number": "89012",
                "student_name": "Maynard Moen",
                "student_class": "10",
                "gender": "laki-laki",
                "school_id": "6c2d532c-b9e0-4031-9f39-32fc98caa745",
                "major": "TP",
                "cp_one": "TS",
                "cp_two": "STS",
                "ce_one": "TS",
                "ce_two": "STS",
                "mcd_one": "TS",
                "mcd_two": "STS",
                "mcd_three": "STS",
                "wwi_one": "TS",
                "wwi_two": "STS",
                "wwi_three": "TS",
                "wwi_four": "SS",
                "wwi_five": "S",
                "pgw_one": "SS",
                "pgw_two": "SS",
                "pgw_three": "S",
                "maturity_career": ""
            },
            {
                "_id": str(uuid.uuid4()),
                "student_parent_number": "90123",
                "student_name": "Jaylan Gleason",
                "student_class": "10",
                "gender": "laki-laki",
                "school_id": "6c2d532c-b9e0-4031-9f39-32fc98caa745",
                "major": "TGB",
                "cp_one": "TS",
                "cp_two": "SS",
                "ce_one": "SS",
                "ce_two": "STS",
                "mcd_one": "TS",
                "mcd_two": "STS",
                "mcd_three": "STS",
                "wwi_one": "S",
                "wwi_two": "SS",
                "wwi_three": "STS",
                "wwi_four": "S",
                "wwi_five": "S",
                "pgw_one": "S",
                "pgw_two": "SS",
                "pgw_three": "TS",
                "maturity_career": ""    
            },
            {
                "_id": str(uuid.uuid4()),
                "student_parent_number": "0123",
                "student_name": "Idella Rodriguez",
                "student_class": "12",
                "gender": "perempuan",
                "school_id": "6c2d532c-b9e0-4031-9f39-32fc98caa745",
                "major": "TGB",       
                "cp_one": "STS",
                "cp_two": "TS",
                "ce_one": "TS",
                "ce_two": "S",
                "mcd_one": "SS",
                "mcd_two": "TS",
                "mcd_three": "TS",
                "wwi_one": "SS",
                "wwi_two": "STS",
                "wwi_three": "TS",
                "wwi_four": "SS",
                "wwi_five": "S",
                "pgw_one": "STS",
                "pgw_two": "TS",
                "pgw_three": "SS",
                "maturity_career": ""
            },
            {
                "_id": str(uuid.uuid4()),
                "student_parent_number": "0124",
                "student_name": "Cathrine Powlowski",
                "student_class": "10",
                "gender": "perempuan",
                "school_id": "6c2d532c-b9e0-4031-9f39-32fc98caa745",
                "major": "TGB",         
                "cp_one": "STS",
                "cp_two": "STS",
                "ce_one": "SS",
                "ce_two": "TS",
                "mcd_one": "SS",
                "mcd_two": "TS",
                "mcd_three": "SS",
                "wwi_one": "SS",
                "wwi_two": "STS",
                "wwi_three": "S",
                "wwi_four": "S",
                "wwi_five": "STS",
                "pgw_one": "SS",
                "pgw_two": "SS",
                "pgw_three": "SS",
                "maturity_career": ""    
            },
        ]

        await db.get_collection('student').insert_many(_student)

    @staticmethod
    async def update(student_id: str, career: str):
        new_data = await db.get_collection('student').update(
            {"_id": student_id}, 
            {"$set": {"maturity_career": career} }
        )

        return new_data
    
    @staticmethod
    async def destroy(id: str):
        student = await db.get_collection('student').find_one({"_id": id})
        if student:
            await db.get_collection('student').delete_one({"_id": id})
            return True

    @staticmethod
    async def destroy_all():
        return await db.get_collection('student').delete_many({})

