from fastapi import APIRouter
from repository.admin import AdminRepo
from models.admin import Admin

router = APIRouter()

@router.get("/users")
async def admin():
    admins = await AdminRepo.retrieve()
    return admins