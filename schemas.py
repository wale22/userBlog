from pydantic import BaseModel

 
# blog schema
class Blog (BaseModel):
    title:str
    body:str
    
    class Config:
        orm_mode = True
        
# blog response model      
class showBlog(Blog):
    pass



#user schema
class User(BaseModel):
    username:str
    password:str
    email:str
    
    class Config:
        orm_mode = True
    
#user response model
class showUser(User):
    pass