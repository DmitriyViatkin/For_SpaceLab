from tortoise import Tortoise, fields
from tortoise.models import Model


async def init_db():
    """Ініціалізація підключення до БД."""
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["models"]}
    )
    await Tortoise.generate_schemas()
