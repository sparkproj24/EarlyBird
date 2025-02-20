from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    password = Column(String)
    
    def __init__(self, firstname, lastname, password):
        self.firstname = firstname
        self.lastname = lastname
        self.password = password

    def __repr__(self):
           return f"User | id={self.id} | firstname={self.firstname}| lastname={self.lastname}"
    

# Create an engine that stores data in a SQLite file
engine = create_engine('sqlite:///earlybird.db', echo=True)

# Create all tables in the engine. This is equivalent to "CREATE TABLE" statements in raw SQL.
Base.metadata.create_all(bind=engine)

# Create a configured "Session" class and create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Example: Add a user
# user = User(firstname='John', lastname='Doe', password='password')
# session.add(user)
# session.commit()

# Example: Query all users
allUsers = session.query(User).all()
print(allUsers)