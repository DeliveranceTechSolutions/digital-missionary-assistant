from uuid import uuid5
from data.user_db import CoreUserDB


class CoreUser(Base):
    # constructor 
    def __init__(self, username, firstname, lastname, email):
        self.cu_id = None
        self.username = None
        self.firstname = None
        self.lastname = None
        self.email = None

    # new_core provides a new user object for use in any service
    # core is used as a prefix for these classes to obfuscate code opposed to having just "User"
    # the naming pattern confuses overtly hostile targets.
    @classmethod
    def new_core(self, username, firstname, lastname, email):
        if get_user_by_email(email) == "":
            setattr(self, 'cu_id', uuid5())
            setattr(self, 'username', username)
            setattr(self, 'firstname', firstname)
            setattr(self, 'lastname', lastname)
            setattr(self, 'email', email)

            return self, None
        else :
            return self, f"{{ firstname lastname }} using {{ email }} has already been created.  Please login or create an additional account"

    # get_user_profile_view will provide a full metadata payload for the frontend requests ONLY!!!
    # @classmethod
    # def get_user_profile_view():
    #     cudb = CoreUserDB()
    #     user, err = cudb.select(self.cu_id)
    #     if err != None:
    #         return None, err
        
    #     return user
    
    @classmethod
    def get_user_by_id():
        cudb = CoreUserDB()
        user, err = cudb.select(self.cu_id)
        if err != None:
            return None, err
        
        return user
    
    @classmethod
    def get_user_by_email():
        cudb = CoreUserDB()
        user, err = cudb.select(self.email)
        if err != None:
            return None, err
        
        return user

