from fastapi import APIRouter
from database.admin_factory import AdminFactory
from database.student_factory import StudentFactory
from repository.student import StudentRepo
from repository.admin import AdminRepo

router = APIRouter()

@router.post('/migrate', tags=['Other'])
async def migrate():
    admin = await AdminFactory.insert_seed()
    await StudentRepo.destroy()
    students = await StudentFactory.insert_seed()
    
    return {
        "admin": admin,
        "students": students
    }