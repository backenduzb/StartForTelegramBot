from models.admin import Admin
import logging

async def create_admin(username: str, tg_id: int):
    exists = await Admin.filter(username=username).exists()
    
    if exists:
        logging.info("Bu Admin allaqachon mavjud!")
    else:
        await Admin.create(
            username=username,
            tg_id=tg_id
        )
        logging.info(f"Admin yaratildi \nusername={username}\ntelegram_id={tg_id}")