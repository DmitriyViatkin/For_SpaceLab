from tortoise import Tortoise
from tortoise.models import Model

async def init_db():
    
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",modules={"models":["models"]}
    )
    
    await Tortoise.generate_schemas()
