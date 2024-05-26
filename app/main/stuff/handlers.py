import time
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from datetime import date
import app.main.stuff.keyboards as kb
from app.main.database.requests import (
    add_diary_entry,
    get_diary_entries,
    track_activity,
    async_session,
    get_activities
)

router = Router()


class DiaryEntryState(StatesGroup):
    content = State()


class ViewDiaryState(StatesGroup):
    date = State()


class TrackActivityState(StatesGroup):
    activity_name = State()
    date = State()
    tracking = State()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет!", reply_markup=kb.main)


@router.message(F.text == "Напоминания")
async def notify(message: Message):
    await message.answer("Выберите тип напоминания", reply_markup=kb.notify_keyb)


@router.callback_query(F.data == "daily_notify")
async def daily_notifications(callback: CallbackQuery):
    await callback.message.answer("Вы выбрали категорию ежедневных напоминаний")
    await callback.message.answer("Ваши ежедневные напоминания:")


@router.message(Command("help"))
async def notify(message: Message):
    await message.answer("Что вы хотели узнать?", reply_markup=kb.help_keyb)


@router.callback_query(F.data == "bot_info")
async def bot_info(callback: CallbackQuery):
    await callback.message.answer(
        "Данный бот Я придумал изначально для себя, но думаю он"
        "будет полезен и вам. В нём есть небольшой функционал для"
        "джорналинга и организации своей деятельности.\n"
        "\nНадеюсь он будет вам полезен)"
    )


@router.callback_query(F.data == "faq")
async def faq(callback: CallbackQuery):
    await callback.message.answer("Пока что здесь ничего нет.")


@router.callback_query(F.data == "functionality")
async def functionality(callback: CallbackQuery):
    await callback.message.answer(
        "Напоминания:\n"
        "Вы можете настраивать свои напоминания и/или включить ежедневные напоминания"
        "они будут помогать вам лучше структурировать свой день и качественнее распределять время.\n"
        "Оповещения:\n"
        "Вы можете включить рассылку с мотивирующими вас сообщениями.\n"
        "Дневник продуктивности и трекер времени:\n"
        'Вы можете заносить "отчёт" о своём дне, а также задавать цели и отслеживать'
        " свою активность в течение дня"
    )


@router.callback_query(F.data == "custom_notify")
async def custom_notifications(callback: CallbackQuery):
    await callback.message.answer("Вы выбрали категорию кастомных напоминаний")
    await callback.message.answer("Введите текст вашего напоминания:")


@router.message(F.text == "Оповещения")
async def notify(message: Message):
    await message.answer("Выберите действие", reply_markup=kb.motivation_keyb)


@router.callback_query(F.data == "on_message")
async def on_message(callback: CallbackQuery):
    await callback.message.answer("Вы включили ежедневную рассылку")


@router.callback_query(F.data == "off_message")
async def off_message(callback: CallbackQuery):
    await callback.message.answer("Вы выключили ежедневную рассылку")




@router.message(F.text == "Дневник продуктивности")
async def diary(message: Message, state: FSMContext):
    await message.answer("Введите запись для дневника:")
    await state.set_state(DiaryEntryState.content)


@router.message(DiaryEntryState.content)
async def add_diary(message: Message, state: FSMContext):
    user_tg_id = message.from_user.id
    entry_content = message.text
    entry_date = date.today()

    await add_diary_entry(user_tg_id, entry_date, entry_content)
    await message.answer("Запись добавлена в дневник!")
    await state.clear()


@router.message(F.text == "Просмотр записей дневника")
async def select_view_date(message: Message, state: FSMContext):
    await message.answer("Выберите дату:", reply_markup=kb.date_keyboard)
    await state.set_state(ViewDiaryState.date)


@router.callback_query(ViewDiaryState.date, F.data == "choose_date")
async def prompt_for_date(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите дату в формате ГГГГ-ММ-ДД:")
    await state.set_state(ViewDiaryState.date)


@router.message(ViewDiaryState.date)
async def process_date_input(message: Message, state: FSMContext):
    try:
        selected_date = date.fromisoformat(message.text)
        await view_diary_entries(message, selected_date)
    except ValueError:
        await message.answer(
            "Некорректный формат даты. Пожалуйста, введите дату в формате ГГГГ-ММ-ДД."
        )
    await state.clear()


async def view_diary_entries(message: Message, entry_date: date):
    user_tg_id = message.from_user.id
    entries = await get_diary_entries(user_tg_id, entry_date)
    if entries:
        response = "\n".join([entry.content for entry in entries])
        await message.answer(f"Ваши записи за {entry_date}:\n{response}")
    else:
        await message.answer("Записей за эту дату нет.")

