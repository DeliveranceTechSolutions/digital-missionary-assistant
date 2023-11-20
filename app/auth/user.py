from uuid import uuid5
from data.user_db import CoreUserDB


class CoreUser(Base):
    # constructor 
    def __init__(self, username, password, firstname, lastname, email):
        self.cu_id = None
        self.username = None
        self.password = None
        self.firstname = None
        self.lastname = None
        self.email = None

    # new_core provides a new user object for use in any service
    # core is used as a prefix for these classes to obfuscate code opposed to having just "User"
    # the naming pattern confuses overtly hostile targets.
    @classmethod
    def new_core(self, username, firstname, lastname, email):
        setattr(self, 'cu_id', uuid5())
        setattr(self, 'username', username)
        setattr(self, 'password', password)
        setattr(self, 'firstname', firstname)
        setattr(self, 'lastname', lastname)
        setattr(self, 'email', email)

        cudb = self.db()
        if get_user_by_email(email) == "":
            cudb.insert(self)
            return self, None
        else :
            cudb.update(self)
            return self, None
            
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
        user, err = self.db.select(self.username)
        if err != None:
            return None, err
        
        return user, None
    
    @classmethod
    def get_user_by_username():
        user, err = self.db.select(self.username)
        if err != None:
            return None, err
        
        return user, None
    
    @classmethod
    def get_user_by_email():
        user, err = self.db.select(self.email)
        if err != None:
            return None, err
        
        return user, None
    
    # subclasses will handle domain connections much like an interface
    class db:
        def __init__(CoreUserDB):
            pass

