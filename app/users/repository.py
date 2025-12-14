from models import User

# database operations
def get_all_users():
    return users_db

def create_user(user: User):
    users_db.append(user)
    return user

def get_user_by_username(username: str):
    for user in users_db:
        if user.username == username:
            return user
    return None

def delete_user(username: str):
    global users_db
    users_db = [user for user in users_db if user.username != username]
