from tortoise import Tortoise, run_async
from config.settings import DATABASE_URL

async def init_db():
    await Tortoise.init(
        db_url=DATABASE_URL,
        modules={"models":["models.admin"]}
    )
    await Tortoise.generate_schemas()