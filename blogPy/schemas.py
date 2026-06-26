from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    author: str
    body: str
    published: bool

    class Config:
        from_attributes = True

class BlogResponse(BaseModel):
    title: str
    author: str
    class Config:
        from_attributes=True

class UserRequest(BaseModel):
    email : str
    name : str
    password : str
    class Config:
        from_attributes=True

class UserResponse(BaseModel):
    email : str
    name : str
    class Config:
        from_attributed=True
