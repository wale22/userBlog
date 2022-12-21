import uvicorn
from fastapi import FastAPI
from components.Router import blog,user
from components import model
from components.database import engine

app=FastAPI()
model.Base.metadata.create_all(engine)
app.include_router(blog.router)
app.include_router(user.router)




if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)