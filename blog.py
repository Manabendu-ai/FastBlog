from pydantic import BaseModel

class Blog(BaseModel):
    id : int
    title : str
    author : str
    content: str
    published : bool
