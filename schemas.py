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
    
class Login(BaseModel):
    email :str
    password : str
    
class Login2(BaseModel):
    id : int
    email :str