from fastapi import APIRouter,Depends,status,HTTPException
from database import get_db
from .. import schemas as s , model, hashing
from sqlalchemy.orm import Session


router=APIRouter()

@router.post('/user',status_code=status.HTTP_201_CREATED, tags=["user"])
def create_user(request: s.User,db:Session=Depends(get_db)):
    user_created=db.query(model.User).filter(model.User.email == request.email).first()
    if user_created:
       HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with {request.email} already exist") 
    user=model.user(username=request.username)