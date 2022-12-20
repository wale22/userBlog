from fastapi import APIRouter,Depends
from database import add_db
from .. import schemas as s , model, hashing
from sqlalchemy.orm import Session


router=APIRouter()


