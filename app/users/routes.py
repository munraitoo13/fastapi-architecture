from fastapi import APIRouter

users_router = APIRouter(prefix="/users")

@users_router.get("/")
async def read_users():
    return [{"user_id": "Alice"}, {"user_id": "Bob"}]
