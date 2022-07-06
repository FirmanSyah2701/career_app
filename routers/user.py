from fastapi import APIRouter
from repository.admin import AdminRepo
from model import Admin

router = APIRouter()

@router.get("/users")
async def admin():
    admins = await AdminRepo.retrieve()
    return admins

@router.post("/users")
async def create(admin: Admin):
    admins = await AdminRepo.insert(admin)
    return {'data': admins}