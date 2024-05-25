from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
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

@router.message(F.text == 'Напоминания')
async def notify(message: Message):
    await message.answer('Выберите тип напоминания', reply_markup=kb.notify)

@router.callback_query(F.data == 'daily_notify')
async def daily_notifications(callback: CallbackQuery):
    await callback.message.answer('Вы выбрали категорию ежедневных напоминаний')
    await callback.message.answer('Ваши ежедневные напоминания:')

@router.message(Command('register'))
async def register(message: Message):
    await message.answer('Введите ваше имя')