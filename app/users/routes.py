from fastapi import APIRouter
from app.users.services import list_users, add_user, remove_user, get_user
from app.users.models import User

users_router = APIRouter(prefix="/users")


@users_router.get("/")
async def read_users():
    """Fetch and return a list of all users."""

    return list_users()


@users_router.post("/")
async def create_user(user: User):
    """Creates a new user and returns the created user."""

    return add_user(user)


@users_router.get("/{username}")
async def read_user(username: str):
    """Fetch and return a user by their username."""

    user = get_user(username)
    if user:
        return user
    return {"error": "User not found"}


@users_router.delete("/{username}")
async def delete_user(username: str):
    """Deletes a user by their username."""

    success = remove_user(username)
    if success:
        return {"message": "User deleted"}
    return {"error": "User not found"}
