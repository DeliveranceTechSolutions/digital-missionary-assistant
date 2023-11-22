from app.auth.auth import Authentication as lock
from app.auth.user import CoreUser

def login(username, password):
    print(username)
    cu = CoreUser(username, password, None, None, None)
    
    user, err = cu.get_user_by_username(username)
    if err != None:
        return err

    unlock = lock.verify_password(user=user, password=password)
    if unlock != False:
        for field, value in vars(dict(user)):
            setattr(cu, field, value)

        return "User is logged in"
    else:
        return "Error: could not login, please check login credentials and try again"