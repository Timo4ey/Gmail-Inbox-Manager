from fastapi import FastAPI

from backend.app.router.routes_email import router_email

app = FastAPI()

app.include_router(router=router_email, 
    prefix='/api',
    tags=["gmail"])