from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from repository.admin import AdminRepo
from utils import access_token
from config import settings 

SECRET_KEY = settings.JWT_SECRET_KEY
ALGORITHM = settings.JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Could not validate credentials",
        headers = { "WWW-Authenticate": "Bearer" },
    )

    token_data = access_token.verify_token(token, credentials_exception)
    user = await AdminRepo.get_by_email(token_data.email)
    if user is None:
        raise credentials_exception
    return {
        "id": user['_id'],
        "email": user['email'],
        "password": user['password'],
        "school_name": user['school_name']
    }