from pydantic import BaseModel,EmailStr
from datetime import datetime

class UserBase(BaseModel): ## base model 
    email:EmailStr

class UserCreate(UserBase): ## used in register
    password : str

class UserLogin(BaseModel): ## used in login can inherit from UserBase but decoupled is better for future
    email : EmailStr
    password : str

class UserResponse(UserBase):
    id : int
    is_active : bool ## why ? for future suppose if we want to disable a user in admin panel etc
    created_at : datetime
    
    class Config:
        from_attribute : True 

class Token(BaseModel):
    access_token : str
    token_type: str = "bearer"

class TokenData(BaseModel):
    user_id : int | None = None