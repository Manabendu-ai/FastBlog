from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    author: str
    body: str
    published: bool

    class Config:
        from_attributes = True   