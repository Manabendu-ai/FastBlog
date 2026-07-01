from fastapi import APIRouter, status, Response, HTTPException
from typing import List

from ..outh2 import get_current_user
from ..schemas import BlogResponse, Blog, UserRequest
from ..repository import blog as repo
from fastapi.params import Depends
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/blog",
    tags=["blogs"]
)

@router.get("/", response_model = List[BlogResponse])
def blogs(db : Session = Depends(get_db), get_current:UserRequest = Depends(get_current_user)): # query parameters
    return repo.get_all(db)

@router.get("/{id}",response_model=BlogResponse)
def get_blog_by_id(id: int,db : Session = Depends(get_db),get_current:UserRequest = Depends(get_current_user), status_code=200):
    return repo.get_blog_by_id(id, db)

@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_blog(blog : Blog, db : Session = Depends(get_db), get_current:UserRequest = Depends(get_current_user)):
    return repo.create_blog(blog, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int, db : Session = Depends(get_db), get_current:UserRequest = Depends(get_current_user)):
    return repo.delete_blog(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(blog : Blog, id:int, db : Session = Depends(get_db), get_current:UserRequest = Depends(get_current_user)):
    return repo.update_blog(blog, id, db)
