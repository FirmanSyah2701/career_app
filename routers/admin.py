from fastapi import APIRouter, Request, status
from fastapi.responses import RedirectResponse
from core.config import templates
from repository.admin import AdminRepo
from form.register import RegisterForm

router = APIRouter(tags=['Register Admin'])

@router.get('/register')
async def register_page(request: Request):
    return templates.TemplateResponse("user/register.html", {"request": request})

@router.post('/register')
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