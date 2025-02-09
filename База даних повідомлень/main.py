from fastapi import FastAPI, HTTPException
from model import User, Post
from date_base import init_db
from api import filling_db

app = FastAPI()

@app.on_event("startup")
async def start_event():
    
    await init_db()
    await filling_db()
    
@app.get("/users/")
async def get_users():
    return await User.all()

@app.get("/users/{user_id}")
async def get_user(user_id:int):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    return user

@app.get("/users/{user_id}/posts/")
async def get_user_posts(user_id: int):
    posts = await Post.filter(user_id=user_id)
    return posts
