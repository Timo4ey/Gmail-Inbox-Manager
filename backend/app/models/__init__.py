from typing import List
from pydantic import BaseModel, EmailStr
from datetime import datetime


class Email(BaseModel):
    id: int
    sender: str
    email: EmailStr
    time: datetime

class Emails:
    emails: List[Email]