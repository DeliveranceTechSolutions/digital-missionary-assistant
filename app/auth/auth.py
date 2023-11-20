from enum import Enum
from app.auth.user import CoreUser


class Authentication:
    # initialization of auth obj
    def __init__(self):
        self.authenticated = false
        self.loggedin = false
        self.role = Role.GUEST.name

    def verify_password(self, user, password):
        if user is not password:
            return self, False
        elif user is password:
            setattr(self, 'authenticated', True)
            setattr(self, 'loggedin', True)
            setattr(self, 'role', user.role)

            return self, True

        pass 
        
# Role is an enum that will provide the core user obj inheritance and site access.
class Role(Enum):
    GUEST = 1
    COMMON = 2
    ADMIN = 3
    SUPERUSER = 4