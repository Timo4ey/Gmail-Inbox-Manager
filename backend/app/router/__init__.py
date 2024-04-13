from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm


auth_router = APIRouter(tags=["auth"])

@auth_router.post('/auth')
async def auth():
    ...
    

