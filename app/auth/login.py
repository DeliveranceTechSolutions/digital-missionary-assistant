from app.auth.auth import Authentication as lock
from app.auth.user import CoreUser

def login(username, password):
    # Create new CoreUser
    # We create this object in order to handle the definition
    cu = CoreUser(username, password, None, None, None)
    
    # Handle retrieving the User from the DB
    cu, err = cu.get_user_by_username()
    if err != None:
        return err

    unlock = lock.verify_password(user=cu, password=password)
    if unlock != False:
        for field, value in vars(dict(user)):
            setattr(cu, field, value)

        return "User is logged in"
    else:
        return "Error: could not login, please check login credentials and try again"
