from fastapi import APIRouter, Depends, status, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from repository.admin import AdminRepo
from utils.hashing import Hash
from utils import access_token, oauth2
from model import Admin

router = APIRouter()

router = APIRouter(tags=['Authentication'])

templates = Jinja2Templates(directory="templates")

@router.get('/login')
def index(request: Request):
    return templates.TemplateResponse("auth/dashboard.html", {"request": request})

@router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    admin = await AdminRepo.get_by_email(form_data.username)
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(admin['password'], form_data.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    token_data = access_token.create_access_token(data={"sub": admin['email']})
    token = jsonable_encoder(token_data)
    content = {
        "access_token": token_data,
        "email": admin['email'],
    }
    response = JSONResponse(content=content)
    response.set_cookie(
        "Authorization",
        value=f"Bearer {token}",
        httponly=True,
        max_age=1800,
        expires=1800,
        samesite="Lax",
        secure=False,
    )

    return response

@router.get('/admin/me')
async def read_users_me(current_user: Admin = Depends(oauth2.get_current_user)):
    return {'data': current_user}

@router.get('/admin/test')
async def read_users_me():
    user = await AdminRepo.get_by_email('smkn1@gmail.com')
    return {'data': user['_id']}