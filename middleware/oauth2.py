from fastapi import HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import RedirectResponse
from repository.admin import AdminRepo
from utils import access_token
from config import settings 

SECRET_KEY = settings.JWT_SECRET_KEY
ALGORITHM = settings.JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(request: Request):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Could not validate credentials",
        headers = { "WWW-Authenticate": "Bearer" },
    )
    
    cookie_authorization: str = request.cookies.get("Authorization")
    if cookie_authorization is None:
        raise credentials_exception

    token: str = cookie_authorization.replace("Bearer ", "")
    
    

    token_data: str = access_token.verify_token(token)
    user = await AdminRepo.get_by_email(token_data)
    
    if user is None:
        raise credentials_exception

    return {
        "id": user['_id'],
        "email": user['email'],
        "school_name": user['school_name']
    }