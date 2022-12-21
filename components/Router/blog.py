from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from database import get_db
from model import Blogs
import schemas as s

router=APIRouter(
    tags=["blogs"],
    prefix="/blog"
)


# creating blog
@router.post('/',status_code=status.HTTP_201_CREATED)
def create_blog(request:s.Blog, db: Session = Depends(get_db)):
    new_blog=Blogs(title=request.title, body=request.body, description=request.description, userId=request.userId)
    print(new_blog)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


#retrieving all the blogs
@router.get('/',status_code=status.HTTP_200_OK)
def retrieve_blogs(db:Session=Depends(get_db)):
    blogs=db.query(Blogs).all()
    return blogs



#retrieving individual blogs
@router.get('/{id}',status_code=status.HTTP_200_OK)
def retrieve_blog(id, db:Session=Depends(get_db)):
    blog=db.query(Blogs).filter(Blogs.id==id).first()
    if not blog:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'There is no blog with the id:{id}')
    return blog

    
# deleting blogs
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id,db:Session=Depends(get_db)):
    db.query(Blogs).filter(Blogs.id == id).delete(synchronize_session=False)
    db.commit()
    return 'Blog with the id {id} has been deleted'



# bulk update of blogs
@router.put('/{id}/all', status_code=status.HTTP_200_OK)
def update_blogs(id, request:s.Blog, db:Session=Depends(get_db)):
    blog=db.query(Blogs).filter(Blogs.id == id)
    if not blog.first():
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='blog does not exist')
   
    blog.update({Blogs.title:request.title,
                 Blogs.body:request.body,
                 Blogs.description:request.description }, synchronize_session=False)
    db.commit() 
    return "done" 
    
    
#individual blog update
@router.put('/{id}', status_code=status.HTTP_200_OK)
def update_blog(id, request:s.Blog, db:Session=Depends(get_db),):
    blog=db.query(Blogs).get(id)
    if not blog:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="blog does not exist ")
    blog.title=request.title 
    blog.body=request.body
    blog.description=request.description
    db.commit()
    
