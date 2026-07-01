from typing import List, Optional

from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    author: str
    body: str
    published: bool
    user_email : str

    class Config:
        from_attributes = True

class UserRequest(BaseModel):
    email : str
    name : str
    password : str
    class Config:
        from_attributes=True

class UserResponse(BaseModel):
    email : str
    name : str
    blogs : List[Blog] = []
    class Config:
        from_attributed=True

class BlogResponse(BaseModel):
    title: str
    author: str
    owner: UserResponse
    class Config:
        from_attributes=True

class Login(BaseModel):
    email: str
    password: str
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None

