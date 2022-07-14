from models.admin import School
from database.mongo import database as db

class SchoolRepo():

    @staticmethod
    async def retrieve():
        schools = []
        collection = db.get_collection('admin').find({'level': 'Admin'})
        async for school in collection:
            schools.append(School(**school))
        return schools