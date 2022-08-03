from database.mongo import database as db
from utils.hashing import Hash
import uuid

class AdminRepo():

    @staticmethod
    async def retrieve():
        _admin = []
        collection = db.get_collection('admin').find()
        async for admin in collection:
            _admin.append(admin)
        return _admin
    
    @staticmethod
    async def get_by_email(email: str):
        admin = await db.get_collection('admin').find_one({'email': email}) 
        return admin

    @staticmethod
    async def insert(email: str, password: str, school_name:str):
        id = str(uuid.uuid4())
        
        _admin = {
            "_id": id,
            "email": email,
            "password": Hash.bcrypt(password),
            "school_name": school_name,
            'level': 'Admin'
        }

        await db.get_collection('admin').insert_one(_admin)

    @staticmethod
    async def update(id: str, data: dict):
        
        admin = await db.get_collection('admin').find_one({'_id': id})
        if(admin):
            update_admin = await db.get_collection('admin').update_one(
                {"_id": id}, 
                {"$set": data }
            )
            return True
        return False
