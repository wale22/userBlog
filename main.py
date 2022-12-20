from fastapi import FastAPI
from Router import blog,user
import uvicorn



app=FastAPI()


app.include_router(blog.router)
app.include_router(user.router)




if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)