from pydantic import BaseModel


# model for user
class User(BaseModel):
    username: str
    email: str
    hashed_password: str
