from fastapi import FastAPI, APIRouter
from app.users.routes import users_router
from app.items.routes import items_router

# app
app = FastAPI()

# router
api_router = APIRouter(prefix="/api")
api_router.include_router(items_router)
api_router.include_router(users_router)

# run server
app.include_router(api_router)
