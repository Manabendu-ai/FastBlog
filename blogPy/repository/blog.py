from sqlalchemy.orm import Session
from fastapi.params import Depends
from fastapi import HTTPException, status
from ..models import Blog as BlogM
from ..schemas import Blog
from ..database import get_db

def get_all(db : Session = Depends(get_db)):
    blogs = db.query(BlogM).all()
    return blogs

def get_blog_by_id(id: int, db : Session = Depends(get_db)):
    blog = db.query(BlogM).filter(BlogM.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with {id} Not Found!"
        )
    return blog

def create_blog(blog : Blog, db : Session = Depends(get_db)):
    new_blog = BlogM(
        title=blog.title,
        author=blog.author,
        body=blog.body,
        published=blog.published,
        user_email=blog.user_email
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete_blog(id: int, db : Session = Depends(get_db)):
    blogs = db.query(BlogM).filter(BlogM.id == id)
    if not blogs.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with {id} Not Found!"
        )
    blogs.delete(synchronize_session=False)
    db.commit()
    return {
        'detail': f'Blog id: {id} Deleted'
    }

def update_blog(blog: Blog, id : int, db : Session = Depends(get_db)):
    blogs = db.query(BlogM).filter(BlogM.id == id)
    if not blogs.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with {id} Not Found!"
        )
    blogs.update(blog.model_dump(), synchronize_session=False)
    db.commit()
    return {
        'detail': f'Blog id: {id} Updated'
    }