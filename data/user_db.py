from sqlalchemy import Column, Integer, String, Sequence, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.auth.user import Role

Base = declarative_base()

class CoreUserDB(Base):
    __tablename__ = 'users'
    cudb_id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50))
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(50))
    role = Column(Role)

    @classmethod
    def _invoke_conn(cls):
        engine = create_engine('sqlite:///example.db')
        Session = sessionmaker(bind=engine, expire_on_commit=True)
        
        return Session()

    @classmethod
    def select(cls, user_param):
        field, value = vars(user_param)
        if field == None or value == None:
            return None, "Error: please provide a parameter for query"
        session = cls._invoke_conn()
        user = session.query(cls).filter_by(field=value).first()

        if user:
            return user, None
        else:
            return None, "Error: could not find desired user"

    @classmethod
    def insert(cls, core_user):
        session = cls._invoke_conn()
        user_db = CoreUserDB(
            username=core_user.username,
            firstname=core_user.firstname,
            lastname=core_user.lastname,
            email=core_user.email,
            role=core_user.role
        )
        session.add(user_db)
        session.commit()
        session.close()

    @classmethod
    def update(cls, core_user_query):
        session = cls._invoke_conn()
        user = session.query(cls).filter_by(email=core_user_query.email).first()

        if user:
            for field, value in vars(core_user_query).items():
                if value is not None and field is not 'cu_id':
                    setattr(cls, field, value)

            session.commit()
            result = "Update is successful!"
        else:
            result = "Error: Could not update User in db"

        session.close()
        
        return result

    @classmethod
    def delete(cls, cudb):
        session = cls._invoke_conn()
        session.delete(cudb)
    
        session.commit()
        session.close()
