from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

import app.main.stuff.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!', reply_markup=kb.main)
    await message.reply('Как дела?')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Помощь')

