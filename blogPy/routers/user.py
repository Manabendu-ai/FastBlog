from fastapi import APIRouter

from ..outh2 import get_current_user
from ..schemas import UserRequest, UserResponse
from ..repository import user as repo
from fastapi.params import Depends
from sqlalchemy.orm import Session
from ..database import get_db
router = APIRouter(
    prefix="/user",
     tags=["users"]
)

@router.post('/create', response_model=UserResponse)
def create_user(userReq: UserRequest, db : Session = Depends(get_db), get_current:UserRequest = Depends(get_current_user)):
    return repo.create_user(userReq, db)

@router.get("/get/{email}", response_model=UserResponse)
def get_user(email : str, db : Session = Depends(get_db), get_current:UserRequest = Depends(get_current_user)):
    return repo.get_user(email, db)
