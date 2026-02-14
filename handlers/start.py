from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

router = Router()

@router.message(F.text == "/start")
async def start(message: types.Message, state: FSMContext):
    await message.answer("Assalomu alaykum")