from fastapi import FastAPI, status, Response, HTTPException
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
@app.post('/blog/create/', status_code=status.HTTP_201_CREATED)
def create_blog(blog : Blog, db : Session = Depends(get_db)):
    new_blog = BlogM(
        title=blog.title,
        author= blog.author,
        body= blog.body,
        published= blog.published
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int, db:Session = Depends(get_db)):
    blogs = db.query(BlogM).filter(BlogM.id == id)
    if not blogs.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with {id} Not Found!"
        )
    blogs.delete(synchronize_session=False)
    db.commit()
    return {
        'detail' : f'Blog id: {id} Deleted'
    }

@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(blog : Blog, id:int, db:Session = Depends(get_db)):
    blogs = db.query(BlogM).filter(BlogM.id == id)
    if not blogs.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with {id} Not Found!"
        )
    blogs.update(blog.model_dump(), synchronize_session=False)
    db.commit()
    return {
        'detail' : f'Blog id: {id} Updated'
    }



@app.get("/blog")
def blogs(limit: int, published : bool, sort : Optional[int] = 1, db : Session = Depends(get_db)): # query parameters
    blogs = db.query(BlogM).all()
    return blogs

@app.get("/blog/{id}")
def get_blog_by_id(id: int, response: Response, db : Session = Depends(get_db), status_code=200):
    # calling the db for the specified blogPy id
    blog = db.query(BlogM).filter(BlogM.id==id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with {id} Not Found!"
        )
    return blog

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