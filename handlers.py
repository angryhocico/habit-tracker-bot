from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я Habit Tracker Bot. 📅\n"
        "Я помогу тебе внедрять полезные привычки.\n"
        "Пока я умею только здороваться, но скоро научусь большему!"
    )