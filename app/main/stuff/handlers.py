from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.main.stuff.keyboards as kb

router = Router()

class Register(StatesGroup):
    name = State()
    age = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!', reply_markup=kb.main)
    await message.reply('Как дела?')


@router.message(F.text == 'Напоминания')
async def notify(message: Message):
    await message.answer('Выберите тип напоминания', reply_markup=kb.notify)

@router.callback_query(F.data == 'daily_notify')
async def daily_notifications(callback: CallbackQuery):
    await callback.message.answer('Вы выбрали категорию ежедневных напоминаний')
    await callback.message.answer('Ваши ежедневные напоминания:')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Помощь')

@router.message(F.text == 'Помощь')
async def notify(message: Message):
    await message.answer('Что вы хотели узнать?', reply_markup=kb.help_keyb)
@router.callback_query(F.data == 'bot_info')
async def daily_notifications(callback: CallbackQuery):
    await callback.message.answer('Данный бот Я придумал изначально для себя, но думаю он'
                                  'будет полезен и вам. В нём есть небольшой функционал для'
                                  'джорналинга и организации своей деятельности.\n'
                                  '\nНадеюсь он будет вам полезен)')

@router.callback_query(F.data == 'faq')
async def daily_notifications(callback: CallbackQuery):
    await callback.message.answer('Я администратор ТГ канал grinder path, создал этого'
                                  'бота для себя и для вас, надеюсь он вам поможет.')


@router.callback_query(F.data == 'daily_notify')
async def daily_notifications(callback: CallbackQuery):
    await callback.message.answer('Вы выбрали категорию ежедневных напоминаний')
    await callback.message.answer('Ваши ежедневные напоминания:')


@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите ваше имя')

@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
