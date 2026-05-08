from pydantic import BaseModel,EmailStr
from datetime import date

class data(BaseModel):
    Name:str
    email:EmailStr
    password:str
    
class deta2(BaseModel):
    query:str
class urespmode(BaseModel):
    Name:str
    email:EmailStr
    dateofopen:date
    class config:
        from_attributes=True
