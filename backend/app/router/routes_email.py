from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import Annotated
from backend.app.models import Email
from datetime import datetime

from fastapi.security import OAuth2PasswordRequestForm


def email_fabic(id: int) -> Email:
    custom_name = "Dave%s" % id
    custom_sander = "Dave%s" % id
    email = "dave%s@gmail.com"% id
    return Email(
        id = id,
        sender=custom_sander,
        email=email,
        time=datetime.now()
    )
    

emails: List[Email] = [email_fabic(i) for i in range(1, 6)]

    


router_email = APIRouter(prefix="/gmail")

@router_email.get('/', tags=["gmail"], response_model=List[Email])
async def get_list() -> List[Email]:
    """Return a list of five emails"""
    data = [{}]
    return emails

@router_email.get('/{email_id}', tags=["gmail"], response_model=Email)
async def get_email(email_id) -> Email:
    return {"email": "email_id"}

@router_email.post('/{email_id}', tags=["gmail"], response_model=Email)
async def post_email(email_id) -> Email:
    return {"email": "email_id"}


@router_email.delete('/{email_id}', tags=["gmail"], response_model=Email)
async def delete_email(email_id) -> Email:
    return {"email": "email_id"}