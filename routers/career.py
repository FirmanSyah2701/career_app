from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from repository.student import StudentRepo
from model import Student

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get('/career')
async def career_page(request: Request):
    students = await StudentRepo.retrieve()
    return templates.TemplateResponse("admin/career.html", {
        "request": request,
        "students": students
    })

@router.post('/career')
async def create(student: Student):
    students = await StudentRepo.insert(student)
    return students