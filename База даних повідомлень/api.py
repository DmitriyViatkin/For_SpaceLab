import httpx
from models import User, Post

API_URL = "https://gorest.co.in/public/v2"


async def fetch_data(end_point):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_URL}/{end_point}")
        return response.json()


'''async def fetch_posts():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_URL}/posts")
        return response.json()'''


async def populate_db():
    """Заповнення БД користувачами та постами, якщо вона порожня."""
    if await User.all().count() == 0:
        users = await fetch_data('users')
        for user_data in users:
            await User.create(
                id=user_data["id"],
                name=user_data["name"],
                email=user_data["email"],
                gender=user_data["gender"],
                status=user_data["status"],
            )

    if await Post.all().count() == 0:
        posts = await fetch_data('posts')
        for post_data in posts:
            user = await User.get_or_none(id=post_data["user_id"])  # Переконайся, що користувач існує
            if user:  # Якщо користувач є
                await Post.create(
                    id=post_data["id"],
                    user=user,
                    title=post_data["title"],
                    body=post_data["body"],
                )
