from fastapi import APIRouter, status, Response, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from ..models import User
from ..database import get_db
from ..schemas import UserRequest, UserResponse
from ..hashing import hashPassword

router = APIRouter(
    prefix="/user",
     tags=["users"]
)

@router.post('/create', response_model=UserResponse)
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

@router.get("/get/{email}", response_model=UserResponse)
def get_user(email : str, db : Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f"user with email {email} not found"
        )
    return user
