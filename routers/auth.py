from fastapi import APIRouter, status, HTTPException, Request, Form
from fastapi.encoders import jsonable_encoder
from fastapi.responses import RedirectResponse
from config import templates
from repository.admin import AdminRepo
from utils.hashing import Hash
from utils import access_token

router = APIRouter(tags=['Authentication'])

@router.get('/register')
async def register_page(request: Request):
    return templates.TemplateResponse("auth/register.html", {"request": request})

@router.post('/register')
async def register(email: str = Form(...), password: str = Form(...), school_name: str = Form(...)):
    admins = await AdminRepo.insert(email, password, school_name)
    return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)

@router.get('/login')
async def login_page(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})

@router.post('/login')
async def login(email: str = Form(...), password: str = Form(...)):
    admin = await AdminRepo.get_by_email(email)
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(admin['password'], password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    token_data = access_token.create_access_token(data={"sub": admin['email']})
    token = jsonable_encoder(token_data)
    content = {
        "access_token": token_data,
        "email": admin['email'],
    }
    response = RedirectResponse(url="/dashboard",status_code=status.HTTP_302_FOUND)
    response.set_cookie(
        "Authorization",
        value=f"Bearer {token}",
        httponly=True,
        max_age=1800,
        expires=1800,
        samesite="lax"
    )
    return response

@router.post('/logout')
async def logout(request: Request):
    response = RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)
    response.delete_cookie('Authorization')
    return response