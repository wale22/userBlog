from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine=create_engine("mysql://wale:walexi202@localhost/memeHouse")
sessionLocal=sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base=declarative_base()


def add_db():
    db=sessionLocal()
    try:
       yield db
    except:
        db.close()