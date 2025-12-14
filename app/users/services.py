from app.users.models import User
from app.users.repository import (
    fetch_all,
    fetch_by_username,
    insert,
    delete_by_username,
)


def list_users() -> list[User]:
    """Fetches and returns a list of all users."""

    users = fetch_all()
    return users


def get_user(username: str) -> User | None:
    """Fetches and returns a user by their username."""

    user = fetch_by_username(username)
    return user


def add_user(user: User) -> User:
    """Inserts a new user into the database."""

    created_user = insert(user)
    return created_user


def remove_user(username: str) -> bool:
    """Deletes a user by their username."""

    success = delete_by_username(username)
    return success
