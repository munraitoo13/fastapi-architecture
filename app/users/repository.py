from app.users.models import User
from app.database.database import users_db


def fetch_all() -> list[User]:
    """Fetch all users from the database."""

    return list(users_db)


def fetch_by_username(username: str) -> User | None:
    """Fetch a user by username from the database."""

    for user in users_db:
        if user.username == username:
            return user
    return None


def insert(user: User) -> User:
    """Insert a new user into the database."""

    users_db.append(user)
    return user


def delete_by_username(username: str) -> bool:
    """Delete a user by username from the database."""

    initial_length = len(users_db)
    users_db[:] = [user for user in users_db if user.username != username]
    if len(users_db) == initial_length:
        return False
    return True
