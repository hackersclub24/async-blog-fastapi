from pydantic import BaseModel

class Create_blog(BaseModel):
    name : str
    email : str
    password : str
    blog : str
    slug : str 
    
class Signup(BaseModel):
    name: str
    email : str
    password : str
    
class login(BaseModel):
    email :str
    password : str
    
class login2(BaseModel):
    id : int
    email :str