from database import Base
from sqlalchemy.types import Text,Integer
from sqlalchemy.schema import  Column


class user(Base):
    __tablename__='blogs'

    
    id=Column(Integer, primary_key=True, index=True)
    title=Column(Text())
    body= Column(Text())
    
    
    
class User(Base):
    __tablename__='users'
    
    id=Column(Integer, primary_key=True, index=True)
    username=Column(Text())
    password= Column(Text())
    email=Column(Text())