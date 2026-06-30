from fastapi import status, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from ..models import User
from ..database import get_db
from ..schemas import UserRequest
from ..hashing import hashPassword

def create_user(userReq: UserRequest, db : Session = Depends(get_db)):
    user = User(
        email=userReq.email,
        name=userReq.name,
        password=hashPassword(userReq.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(email : str, db : Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f"user with email {email} not found"
        )
    return user