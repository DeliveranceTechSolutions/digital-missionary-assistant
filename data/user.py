from uuid import uuid5

class CoreUser:

    # constructor 
    def __init__(self, firstname, lastname, email):
        self.id = uuid5()
        self.username = ""
        self.firstname = ""
        self.lastname = ""
        self.email = ""

    # core is used 
    @classmethod
    def new_core(self, username, password, firstname, lastname, email):
        if get_user_by_email(email) != "":
            self.username = username
            self.firstname = firstname
            self.lastname = lastname
            self.email = email

            return self, None
        else :
            return self, f"{{ firstname lastname }} using {{ email }} has already been created.  Please login or create an additional account"

    @classmethod
    def validate(self, username, password):
        
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

