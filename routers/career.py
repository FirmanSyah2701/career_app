from fastapi import APIRouter, Request, Depends, status
from fastapi.responses import RedirectResponse
from config import templates
from repository.student import StudentRepo
from models.student import Student
from models.admin import ShowAdmin
from middleware import oauth2
from utils import kmeans

router = APIRouter()

@router.get('/career')
async def career_page(request: Request, current_user: ShowAdmin = Depends(oauth2.get_current_user)):
    students = await StudentRepo.retrieve_school_id(current_user['id'])
    data = kmeans.predict(students)
    return templates.TemplateResponse("admin/career.html", {
        "request": request,
        "students": data,
        "title": "Data Karir"
    })

""" @router.post('/career/seed')
async def create_seed():
    await StudentRepo.destroy()
    students = await StudentRepo.insert_seed()
    return students """

@router.post('/career')
async def create(student: Student = Depends(Student.as_form)):
    students = await StudentRepo.insert(student)
    return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)

@router.delete('/career/{id}')
async def delete(id: str):
    student = await StudentRepo.destroy(id)
    return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)

@router.get('/export')
async def export(current_user: ShowAdmin = Depends(oauth2.get_current_user)):
    students = await StudentRepo.retrieve_school_id(current_user['id'])
    data = kmeans.predict(students, 'export')
    return data
    