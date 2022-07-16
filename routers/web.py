from fastapi import APIRouter, Request, Depends, status
from fastapi.responses import RedirectResponse
from core.config import templates
from middleware import oauth2
from models.admin import ShowAdmin
from repository.school import SchoolRepo
from repository.student import StudentRepo
from utils import kmeans
from form.career import CareerForm

router = APIRouter()

@router.get('/', tags=['Career for student'])
async def index(request: Request):
    schools = await SchoolRepo.retrieve()
    return templates.TemplateResponse("user/form_career.html", {
        "request": request, 
        'schools': schools
    })

@router.post('/', tags=['Career for student'])
async def create(request: Request):
    schools = await SchoolRepo.retrieve()
    form = CareerForm(request)
    await form.load_data()
    if await form.is_valid():
        try:
            new_student = await StudentRepo.insert(form)
            return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
        except Exception as e:
            print(e)
            context = form.__dict__.copy()
            context.update({"schools": schools})
            form.__dict__.get("errors").append("Incorrect")
            return templates.TemplateResponse(
                "user/form_career.html", 
                context=context
            )
    context = form.__dict__.copy()
    context.update({"schools": schools})
    return templates.TemplateResponse(
        "user/form_career.html", 
        context=context
    )
    
@router.get('/dashboard', tags=['Dashboard'])
async def dashboard(request: Request, current_user: ShowAdmin = Depends(oauth2.get_current_user)):
    if current_user['msg']:
        return templates.TemplateResponse("auth/login.html", {
            "request": request,
            "errors": [current_user['msg']]
        })
    students = await StudentRepo.retrieve()
    data = kmeans.predict(students, current_user['id'], "dashboard")
    return templates.TemplateResponse("admin/dashboard.html", {
        "request": request,
        "data_count": data,
        "title": "Dashboard"
    })