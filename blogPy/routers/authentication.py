from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session
from ..schemas import Login
from ..models import User
from ..database import get_db
from ..hashing import verify
router = APIRouter()

@router.post('/login', tags=["Authentication"])
def login(request: Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid Credentials!"
        )

    if not verify(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Incorrect Password!"
        )

    # generate JWT Token
    return user