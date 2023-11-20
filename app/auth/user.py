from uuid import uuid5


class CoreUser(Base):
    # constructor 
    def __init__(self, username, firstname, lastname, email):
        self.cu_id = None
        self.username = None
        self.firstname = None
        self.lastname = None
        self.email = None

    # core is used 
    @classmethod
    def new_core(self, username, firstname, lastname, email):
        if get_user_by_email(email) != "":
            setattr(self, 'cu_id', uuid5())
            setattr(self, 'username', username)
            setattr(self, 'firstname', firstname)
            setattr(self, 'lastname', lastname)
            setattr(self, 'email', email)

            return self, None
        else :
            return self, f"{{ firstname lastname }} using {{ email }} has already been created.  Please login or create an additional account"

    @classmethod
    def get_user():
        pass

    @classmethod
    def get_user_profile_view():
        pass
    
    @classmethod
    def get_user_by_id():
        pass
    
    @classmethod
    def get_user_by_email():
        pass

