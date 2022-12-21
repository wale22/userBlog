from pydantic import BaseModel
from typing import List


# blog schema
class Blog (BaseModel):
    title:str
    body:str
    userId:int
    class Config:
        orm_mode = True
        



#user schema
class User(BaseModel):
    username:str
    password:str
    email:str
    
    class Config:
        orm_mode = True

    
#user response model
class showUser():
    username:str
    password:str
    email:str
    blogs:List[Blog]=[]
    class Config:
        orm_mode = True




class ShowBlog(BaseModel):
    title: str
    body:str
    creator: showUser

    class Config():
        orm_mode=True