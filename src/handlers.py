from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from src.text import start_handler
from src.responces import check_geo
from src.database import check_user_exists, append_user

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message):
    if check_user_exists(message.from_user.id):
        await message.answer(f"Добро пожаловать {message.from_user.full_name}!")
    else:
        await message.answer(start_handler)
        append_user(message.from_user.id, "Орел")


@router.message(Command("help"))
async def command_help_handler(message: Message):
    await message.answer("Hello!")
