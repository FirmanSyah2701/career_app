from fastapi import APIRouter, Request, Depends, status
from fastapi.responses import RedirectResponse
from core.config import templates
from repository.student import StudentRepo
from models.admin import ShowAdmin
from middleware import oauth2
from utils import kmeans

router = APIRouter(tags=["Career"])

@router.get('/career')
async def career_page(request: Request, current_user: ShowAdmin = Depends(oauth2.get_current_user)):
    if current_user['msg']:
        return templates.TemplateResponse("auth/login.html", {
            "request": request,
            "errors": [current_user['msg']]
        })
    students = await StudentRepo.retrieve()
    data = kmeans.predict(students, current_user)
    school_id = ""
    if current_user['school_name']:
        school_id = current_user['id']
    return templates.TemplateResponse("admin/career.html", {
        "request": request,
        "students": data,
        "school_id": school_id,
        "title": "Data Karir"
    })

@router.get('/career/{id}')
async def delete(request: Request, id: str, current_user: ShowAdmin = Depends(oauth2.get_current_user)):
    if current_user['msg']:
        return templates.TemplateResponse("auth/login.html", {
            "request": request,
            "errors": [current_user['msg']]
        })
    delete_student = await StudentRepo.destroy(id)
    return RedirectResponse(url="/career", status_code=status.HTTP_302_FOUND)

@router.get('/career/export/{id}')
async def export(request: Request, id: str, current_user: ShowAdmin = Depends(oauth2.get_current_user)):
    if current_user['msg']:
        return templates.TemplateResponse("auth/login.html", {
            "request": request,
            "errors": [current_user['msg']]
        })
    students = await StudentRepo.retrieve()
    data = kmeans.predict(students, current_user, 'export')
    return data