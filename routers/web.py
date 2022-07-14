from fastapi import APIRouter, Request, Depends
from config import templates
from middleware import oauth2
from models.admin import ShowAdmin
from repository.school import SchoolRepo
from repository.student import StudentRepo
from utils import kmeans

router = APIRouter()

@router.get('/')
async def index(request: Request):
    schools = await SchoolRepo.retrieve()
    return templates.TemplateResponse("user/form_career.html", {
        "request": request, 
        'schools': schools
    })

@router.get('/dashboard')
async def dashboard(request: Request, current_user: ShowAdmin = Depends(oauth2.get_current_user)):
    students = await StudentRepo.retrieve_school_id(current_user['id'])
    data = kmeans.predict(students, "dashboard")
    return templates.TemplateResponse("admin/dashboard.html", {
        "request": request,
        "data_count": data,
        "title": "Dashboard"
    })