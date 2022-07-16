from fastapi import APIRouter, status, HTTPException, Request, Form
from fastapi.encoders import jsonable_encoder
from fastapi.responses import RedirectResponse
from core.config import templates
from repository.admin import AdminRepo
from utils.hashing import Hash
from utils import access_token
from form.login import LoginForm

router = APIRouter(tags=['Authentication'])

@router.get('/login')
async def login_page(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})

@router.post('/login')
async def login(request: Request):
    form = LoginForm(request)
    await form.load_data()
    if await form.is_valid():
        try:
            admin = await AdminRepo.get_by_email(form.email)
            if not admin:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail=f"Invalid Credentials")
            if not Hash.verify(admin['password'], form.password):
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
        except Exception as e:
            print(e)
            form.__dict__.get("errors").append("Incorrect Email or Password")
            return templates.TemplateResponse("auth/login.html", form.__dict__)
    return templates.TemplateResponse("auth/login.html", form.__dict__)

@router.post('/logout')
async def logout(request: Request):
    response = RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)
    response.delete_cookie('Authorization')
    return response