from fastapi import APIRouter, Request
from controller.authController import login

router = APIRouter(
    prefix="/api/auth",
    tags=["auth"]
)

@router.post("/login")
async def login_route(request: Request):
    return await login(request)