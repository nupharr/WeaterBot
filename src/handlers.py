from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from src.database import append_user, check_user_exists, get_location, delete_user
from src.responces import get_weater
from src.text import start_handler

router = Router()


class Reg(StatesGroup):
    city = State()


@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext):
    if check_user_exists(message.from_user.id):
        await message.answer(
            f"Добро пожаловать {message.from_user.full_name}!\nВаше местоположение - {get_location(message.from_user.id)["name"]}\nВоспользуйтесь командой /weather\nЕсли хотите удалить город воспользуйтесь /del_city"
        )
    else:
        await state.set_state(Reg.city)
        await message.answer(
            "Привет!\nДля начала я должен узнать твоё местоположение.\nНапиши название своего города."
        )


@router.message(Reg.city)
async def reg_city(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    data = await state.get_data()
    append_user(message.from_user.id, data["city"])
    await state.clear()
    await message.answer(
        "Отлично! Город успешно добавлен.\nВоспользуйтесь командой /weather"
    )


@router.message(Command("weather"))
async def command_help_handler(message: Message):
    await message.answer(
        get_weater(
            get_location(message.from_user.id)["lat"],
            get_location(message.from_user.id)["lon"],
        )
    )


@router.message(Command("del_city"))
async def command_delete_city(message: Message):
    delete_user(message.from_user.id)
    await message.answer("Город удалён!\nВоспользуйтесь командой /start")
