from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker
import os

class Database:
    def __init__(self):
        # Retrieve database connection details from environment variables
        db_url = os.environ.get('DATABASE_URL', 'sqlite:///:memory:')
        self.engine = create_engine(db_url)
        self.metadata = MetaData()

    def get_engine(self):
        return self.engine

class Reader(Database):
    def __init__(self):
        super().__init__()

    def query_index(self, table):
        with self.engine.connect() as connection:
            result = connection.execute(table.select()).fetchall()
            return result

    def query_free(self, table):
        with self.engine.connect() as connection:
            result = connection.execute(table.select())


class Writer(Database):
    def __init__(self):
        super().__init__()

    def create_dynamic_table(self, tablename, **columns):
        metadata = MetaData()

        dynamic_table = Table(
            tablename,
            metadata,
            Column('id', Integer, primary_key=True),
            *(Column(name, String) for name in columns),
        )

        metadata.create_all(self.engine)
        return dynamic_table

    def insert_data(self, table, data):
        with self.engine.connect() as connection:
            insert_stmt = table.insert().values(**data)
            connection.execute(insert_stmt)

class Manager(Reader, Writer):
    def __init__(self):
        super().__init__()

# User class inheriting from DBReader and DBWriter
class User(Manager):
    def __init__(self, engine):

        # Create a dynamic user table
        self.user_table = self.create_dynamic_table('user_table', name='VARCHAR(255)', age='INTEGER')

    def find_all_users(self):
        return self.query_index(self.user_table)

    def add_user(self, name, age):
        data = {'name': name, 'age': age}
        self.insert_data(self.user_table, data)

# # Group class inheriting from DBReader and DBWriter
# class Group(Reader, Writer):
#     def __init__(self, engine):
#         Reader.__init__(self, engine)
#         Writer.__init__(self, engine)

#         # Create a dynamic group table
#         self.group_table = self.create_dynamic_table('group_table', group_name='VARCHAR(255)')

#     def get_groups(self):
#         return self.query_data(self.group_table)

#     def add_group(self, group_name):
#         data = {'group_name': group_name}
#         self.insert_data(self.group_table, data)

# Create an SQLite in-memory database engine
engine = create_engine('sqlite:///:memory:')

manager = Manager()
# Instantiate User and Group classes
manage_user = User(manager)

user.manager.find_all_users()
manage_user.data.by_adding_user()
