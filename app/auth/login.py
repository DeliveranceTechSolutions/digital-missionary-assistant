from auth import Authentication as lock
from user import get_user_by_username

def login(username, password):
    user = get_user_by_username(username)
    unlock = lock.verify_password(user, password)
    if unlock:
        user.loggedin = unlock.loggedin
        user.role = unlock.role

        return "User is logged in"
    else:
        return "Error: could not login, please check login credentials again"