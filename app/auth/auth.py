from enum import Enum
from data.user import CoreUser

class Authentication:
    # initialization of auth obj
    def __init__(self):
        self.authenticated = false
        self.role = Role.GUEST.name

    def verify_password(self, password):
        
# Role is an enum that will provide the core user obj inheritance and site access.
class Role(Enum):
    GUEST = 1
    COMMON = 2
    ADMIN = 3
    SUPERUSER = 4