from fastapi import APIRouter, status, Response, HTTPException
from typing import List, Optional
from ..schemas import BlogResponse, Blog
from sqlalchemy.orm import Session
from fastapi.params import Depends
from ..models import Blog as BlogM
from ..database import get_db

router = APIRouter(
    prefix="/blog",
    tags=["blogs"]
)

@router.get("/", response_model = List[BlogResponse])
def blogs( db : Session = Depends(get_db)): # query parameters
    blogs = db.query(BlogM).all()
    return blogs

@router.get("/{id}",response_model=BlogResponse)
def get_blog_by_id(id: int, response: Response, db : Session = Depends(get_db), status_code=200):
    # calling the db for the specified blogPy id
    blog = db.query(BlogM).filter(BlogM.id==id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with {id} Not Found!"
        )
    return blog

@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_blog(blog : Blog, db : Session = Depends(get_db)):
    new_blog = BlogM(
        title=blog.title,
        author= blog.author,
        body= blog.body,
        published= blog.published,
        user_email=blog.user_email
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
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

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
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
