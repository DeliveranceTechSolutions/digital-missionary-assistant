from sqlalchemy import Column, Integer, String, Sequence, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


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

class CoreUserDB():
    @classmethod
    def _invoke(cls):
        engine = create_engine('sqlite:///example.db')
        Session = sessionmaker(bind=engine, expire_on_commit=True)
        
        return Session(), CoreUserDBWriter()

    @classmethod
    def select(cls, user_param):
        print(user_param.items())
        field, value = zip(*user_param.items())

        
        if field == None or value == None:
            return None, "Error: please provide a parameter for query"
        session, writer = cls._invoke()
        user = session.query(cls).filter_by(field=value).first()

        if user:
            return user, None
        else:
            return None, "Error: could not find desired user"

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
        session.add(writer)
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
