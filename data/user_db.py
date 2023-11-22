from sqlalchemy import Column, Integer, String, Sequence, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..app import RequestFormatter as log
from flask import current_app


Base = declarative_base()

class CoreUserDBWriter(Base):
    __tablename__ = 'users'
    cudb_id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50))
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(50))
    role = Column(String(50))

    def _set(cls):
        # Assuming you have a dictionary with attribute names and values
        attributes = {
            'cudb_id': 123,
            'username': 'john_doe',
            'firstname': 'John',
            'lastname': 'Doe',
            'email': 'john@example.com',
            'role': 'user'
        }

        for attr, value in attributes.items():
            setattr(cls, attr, value)
    
    @classmethod
    def select(cls, session, user_param):
        key, val = zip(*user_param.items())
        field = str(key[0])
        value = str(val[0])
        print(field, value)
        if field == None and value == None:
            return None, "Error: please provide a parameter for query"

        user = session.query(getattr(cls, field)).filter(getattr(cls, field) == value).first()

        if user:
            return user, None
        else:
            return None, "Error: could not find desired user"


class CoreUserDB():
    @classmethod
    def _invoke(cls):
        engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(engine)
        
        Session = sessionmaker(bind=engine, expire_on_commit=True)
        
        return Session(), CoreUserDBWriter()

    @classmethod
    def insert(cls, core_user):
        session, writer = cls._invoke()
        # check for redundant sql entries
        writer._set(
            username=core_user.username,
            firstname=core_user.firstname,
            lastname=core_user.lastname,
            email=core_user.email,
            role=core_user.role
        )
        
        session.commit()
        session.close()

    @classmethod
    def update(cls, core_user_query):
        session, writer = cls._invoke()
        user = session.query(writer).filter_by(email=core_user_query.email).first()

        if user:
            for field, value in vars(core_user_query).items():
                if value != None and field != 'cu_id':
                    setattr(writer, field, value)

            session.commit()
            result = "Update is successful!"
        else:
            result = "Error: Could not update User in db"

        session.close()
        
        return result

    @classmethod
    def delete(cls, cudb):
        session = cls._invoke()
        session.delete(cudb)
    
        session.commit()
        session.close()
