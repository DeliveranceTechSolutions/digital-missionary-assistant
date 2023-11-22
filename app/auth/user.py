from uuid import uuid5
from data.user_db import CoreUserDB
from data.tools import Reader, Writer


class CoreUser(Reader, Writer):
    self.cu_id = None
    self.username = None
    self.password = None
    self.firstname = None
    self.lastname = None
    self.email = None

    def __init__(self, engine):
        Reader.__init__(self, engine)
        Writer.__init__(self, engine)

        # Create a dynamic user table
        self.user_table = self.create_dynamic_table('user_table', name='VARCHAR(255)', age='INTEGER')
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
    
    @classmethod
    def get_user_by_id(self):
        self.query_index(self.user_table)
    
    @classmethod
    def get_user_by_username(self, usrn):
        db = self.db()
        session, writer = db._invoke()
        
        user, err = writer.select(session, dict(username=usrn))
        if err != None:
            return None, err

        return user.username, None

    @classmethod
    def get_user_by_email(self):
        user, err = self.db().select(self.email)
        if err != None:
            return None, err
        
        return user, None

    def db():
        return CoreUserDB()

