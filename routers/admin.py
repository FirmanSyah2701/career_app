from fastapi import APIRouter, Request, status, Depends
from fastapi.responses import RedirectResponse
from core.config import templates
from models.admin import ShowAdmin
from middleware import oauth2
from repository.admin import AdminRepo
from form.register import RegisterForm
from form.profile import ProfileForm

router = APIRouter()

@router.get('/register', tags=['Register Admin'])
async def register_page(request: Request):
    return templates.TemplateResponse("user/register.html", {"request": request})

@router.post('/register', tags=['Register Admin'])
async def register(request: Request):
    form = RegisterForm(request)
    await form.load_data()
    if await form.is_valid():
        try:
            admin_exists = await AdminRepo.get_by_email(form.email)
            if admin_exists:
                form.__dict__.get("errors").append("Akun dengan email tersebut sudah ada")
                return templates.TemplateResponse("user/register.html", form.__dict__)
            
            admins = await AdminRepo.insert(form.email, form.password, form.school_name)
            return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)
        except Exception as e:
            print(e)
            form.__dict__.get("errors").append("Pengisian data tidak valid")
            return templates.TemplateResponse("user/register.html", form.__dict__)
    return templates.TemplateResponse("user/register.html", form.__dict__)

@router.get('/profile', tags=['Profile Admin'])
async def profile_page(request: Request, current_user: ShowAdmin = Depends(oauth2.get_current_user)):
    return templates.TemplateResponse("admin/profile.html", {
        'request': request,
        'data': current_user
    })

@router.post('/profile', tags=['Profile Admin'])
async def change_profile(request: Request, current_user: ShowAdmin = Depends(oauth2.get_current_user)):
    form = ProfileForm(request)
    await form.load_data()
    if await form.is_valid():
        try:
            school_name = form.school_name or ""
            admin = await AdminRepo.update(current_user['id'], form.email, "")
            return templates.TemplateResponse("admin/profile.html", {
                "request": request,
                "data": current_user,
                "success": "Data berhasil diubah"
            })
        except Exception as e:
            print(e)
            context = form.__dict__.copy()
            context.update({"data": current_user})
            form.__dict__.get("errors").append("Pengisian data tidak valid")
            return templates.TemplateResponse("admin/profile.html", form.__dict__)
    context = form.__dict__.copy()
    context.update({"data": current_user})
    return templates.TemplateResponse("admin/profile.html", context=context)