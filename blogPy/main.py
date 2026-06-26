import uvicorn
from fastapi import FastAPI, Depends
from typing import Optional
from fastapi.params import Depends
from sqlalchemy.orm import Session
from .models import Base, Blog as BlogM
from .database import engine, SessionLocal
from .schemas import Blog
app = FastAPI()

Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post('/blog/create/')
def create_blog(blog : Blog, db : Session = Depends(get_db)):
    new_blog = BlogM(
        title=blog.title,
        author= blog.author,
        body= blog.author,
        published= blog.published
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog")
def blogs(limit: int, published : bool, sort : Optional[int] = 1): # query parameters
    # Get 10 published Blogs

    return {
        'data': {
            'limit' : limit,
            'published' : published
        }
    }

@app.get("/blog/{id}")
def get_blog_by_id(id: int):
    # calling the db for the specified blogPy id
    return {
        "data" : {
            "blogPy" : {
                "id" : id,
                "msg" : "Heyy hello"
            }
        }
    }

@app.get("/author")
def author():
    return {
        "data" : {
            "first_name" : "Manabendu",
            "last_name" : 'Karfa'
        }
    }

# changing the default port
#
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)