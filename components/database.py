from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .url import URL

engine=create_engine(URL)
sessionLocal=sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base=declarative_base()


def get_db():
    db=sessionLocal()
    try:
       yield db
    except:
        db.close()
