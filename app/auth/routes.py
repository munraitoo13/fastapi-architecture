from fastapi import APIRouter, Response
from app.auth.services import register, login
from app.auth.schemas import UserLogin, UserRegister

auth_router = APIRouter(prefix="/auth")


@auth_router.post("/register")
async def register_user(user: UserRegister):
    success = register(user)
    if success:
        return {"message": "User registered successfully"}
    return {"message": "Registration failed"}


@auth_router.post("/login")
async def login_user(user: UserLogin, response: Response):
    token = login(user)
    if token:
        response.set_cookie(key="token", value=token)
        return {"message": "Login successful"}
    return {"message": "Invalid credentials"}
