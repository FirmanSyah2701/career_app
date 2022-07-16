from database.mongo import database as db
from utils.hashing import Hash
import uuid

class AdminFactory():
    @staticmethod
    async def insert_seed():
        _admin = [
            {
                "_id": str(uuid.uuid4()),
                "email": 'admin123@gmail.com',
                "password": Hash.bcrypt('admin123'),
                'level': 'Super Admin'
            },
            {
                "_id": str(uuid.uuid4()),
                "email": 'smk1@gmail.com',
                "password": Hash.bcrypt('smk1123'),
                'level': 'Admin'
            },
            {
                "_id": str(uuid.uuid4()),
                "email": 'smk2@gmail.com',
                "password": Hash.bcrypt('smk2'),
                'level': 'Admin'
            },
        ]

        await db.get_collection('admin').insert_one(_admin)