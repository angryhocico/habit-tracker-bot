from aiogram import Router, types
from aiogram.filters import Command
from database import add_user

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    user = message.from_user
    # пробуем добавить в БД
    is_new = add_user(user.id, user.username)
    
    text = "Привет! Я Habit Tracker Bot. 📅"
    if is_new:
        text += "\nЯ тебя запомнил! Добро пожаловать."
    else:
        text += "\nРад видеть тебя снова!"

    await message.answer(text)