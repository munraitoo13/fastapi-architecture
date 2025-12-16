import os
from app.users.models import User
from app.users.services import add_user, get_user
from app.auth.schemas import UserLogin, UserRegister
from dotenv import load_dotenv
import jwt
import bcrypt
import datetime

load_dotenv()


def register(user: UserRegister) -> bool:
    salt = bcrypt.gensalt()
    password_bytes = user.password.encode()
    hashed_bytes = bcrypt.hashpw(password_bytes, salt)
    hashed_bytestring = hashed_bytes.decode()

    new_user = User(
        username=user.username, email=user.email, hashed_password=hashed_bytestring
    )

    created_user = add_user(new_user)

    return created_user is not None


def login(user: UserLogin) -> str | None:
    existing_user = get_user(user.username)

    if existing_user:
        password_bytes = user.password.encode()
        hashed_bytes = existing_user.hashed_password.encode()

        if bcrypt.checkpw(password_bytes, hashed_bytes):
            exp = os.getenv("JWT_EXPIRATION_HOURS", "1")
            secret = os.getenv("JWT_SECRET")
            algorithm = os.getenv("JWT_ALGORITHM")

            payload = {
                "sub": user.username,
                "exp": datetime.datetime.now() + datetime.timedelta(hours=int(exp)),
            }

            token = jwt.encode(
                payload,
                secret,
                algorithm,
            )

            return token

    return None
