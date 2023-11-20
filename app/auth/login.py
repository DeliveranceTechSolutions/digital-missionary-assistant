from app.auth.auth import Authentication as lock
from user import CoreUser

def login(username, password):
    cu = CoreUser()
    
    user = cu.get_user_by_username(username)
    unlock = lock.verify_password(user, password)
    if unlock:
        for field, value in vars(user):
            setattr(cu, field, value)

        return "User is logged in"
    else:
        return "Error: could not login, please check login credentials again"