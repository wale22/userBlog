from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..model import Users
from ..hashing import Hash
from .. import schemas as s

router=APIRouter(
    tags=["users"],
    prefix="/user"
)


#user registration
@router.post('/register',status_code=status.HTTP_201_CREATED)
def create_user(request: s.User,db:Session=Depends(get_db)):
   user_created=db.query(Users).filter(Users.email == request.email).first()
   if user_created:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {request.email} already exist")
   user=Users(username=request.username,email=request.email,password=Hash.encrypt(request.password))
   db.add(user)
   db.commit()
   db.refresh(user)
   return "user has been created"


# authentication
@router.post('/login',status_code=status.HTTP_200_OK,response_model=s.showUser)
def login(request:s.authenticate, db:Session=Depends(get_db)):
   user=db.query(Users).filter(Users.email == request.email).first()
   if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with {request.email}  does not exist") 
   if Hash.decrypt(request.password,user.password):
      return user
   raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"invalid password") 
   
   
  
# getting individual user 
@router.get('/{id}',response_model=s.showUser,status_code=status.HTTP_200_OK)
def retrieve_user(id,db:Session=Depends(get_db)):
   user=db.query(Users).filter(Users.id == id).first()
   if not user:
      raise HTTPException(status_codes=status.HTTP_404_NOT_FOUND,detail="user does not exist")
   return user


#retrieving all the users
@router.get('/',status_code=status.HTTP_200_OK)
def retrieve_users(db:Session=Depends(get_db)):
   users=db.query(Users).all()
   return users


#updating user
@router.put('/{id}', status_code=status.HTTP_200_OK)
def update_user(id, request:s.User, db:Session=Depends(get_db),):
   user=db.query(Users).get(id)
   if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="blog does not exist ")
   user.username=request.username  
   user.email=request.email
   user.password=Hash.encrypt(request.password)
   db.commit()
   db.refresh(user)
   return user

#deleting user
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id,db:Session=Depends(get_db)):
   db.query(Users).filter(Users.id == id).delete(synchronize_session=False)
   db.commit()
   return 'Blog with the id {id} has been deleted'
