from pydantic import BaseModel
from typing import List


# blog schema
class Blog (BaseModel):
    title:str
    body:str
    userId:int
    description:str
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
class showUser(BaseModel):
    id:int
    username:str
    email:str
    blogs:List[Blog]=[]
    class Config:
        orm_mode = True


class usr(BaseModel):
    id:int
    username:str
    email:str
    class Config:
        orm_mode = True

class ShowBlog(BaseModel):
    id:int
    creator: usr
    title:str
    body:str
    description:str
    class Config:
        orm_mode = True


class authenticate(BaseModel):
    email:str
    password:str