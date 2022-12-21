from database import Base
from sqlalchemy.types import Text,Integer
from sqlalchemy.schema import  Column,ForeignKey
from sqlalchemy.orm import relationship




    
    
class User(Base):
    __tablename__='users'
    id=Column(Integer, primary_key=True, index=True)
    username=Column(Text)
    password= Column(Text)
    email=Column(Text)
    blog=relationship("Blogs", back_populates="creator")



class Blogs(Base):
    __tablename__='blogs'
    id=Column(Integer, primary_key=True, index=True)
    title=Column(Text())
    body= Column(Text())
    userId=Column(Integer,ForeignKey(User.id))
    creator=relationship("User", back_populates="blog")
    