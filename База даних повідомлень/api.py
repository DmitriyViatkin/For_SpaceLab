import  httpx 
from model import User, Post
API_URL = "https://gorest.co.in/public/v2"

async def get_data (end_point):
    
    async with httpx.AsyncClient() as client:
        
        response = await client.get(f"{API_URL}/"+end_point)
        return response.json()
    
async def filling_db():
    
    if await User.all().count()==0:
        users = await get_data("users")
        for user_data in users:
            await User.create(
                id=user_data["id"],
                name = user_data["name"],
                email=user_data["email"],
                gender = user_data["gender"],
                status=user_data["status"]
            )
    if await Post.all().count == 0:
        
        posts= await get_data("posts")
        for post_data in posts:
            await Post.create(
                id=post_data["id"],
                user=post_data["user_id"],
                title=post_data["title"],
                body=post_data['body'])