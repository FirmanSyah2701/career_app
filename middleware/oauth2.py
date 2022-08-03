from fastapi import Request
from fastapi.security import OAuth2PasswordBearer
from repository.admin import AdminRepo
from utils import access_token
from core.config import settings

SECRET_KEY = settings.JWT_SECRET_KEY
ALGORITHM = settings.JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(request: Request):
    cookie_authorization: str = request.cookies.get("Authorization")
    if cookie_authorization is None:
        return {
            "msg": "Tidak dapat memvalidasi kredensial"
        }

    token: str = cookie_authorization.replace("Bearer ", "")
    
    token_data: str = access_token.verify_token(token)
    user = await AdminRepo.get_by_email(token_data)
    school = ""
    if 'school_name' in user: school = user['school_name']
    return {
        "id": user['_id'],
        "email": user['email'],
        "name": user['name'],
        "school_name": school,
    }