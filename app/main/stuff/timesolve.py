@router.message(F.text == "Трекер времени")
async def start_tracking(message: Message, state: FSMContext):
    await message.answer("Введите название активности:")
    await state.set_state(TrackActivityState.activity_name)


@router.message(TrackActivityState.activity_name)
async def enter_activity_name(message: Message, state: FSMContext):
    activity_name = message.text
    await state.update_data(activity_name=activity_name)
    await message.answer(
        f"Начинаю отслеживать активность '{activity_name}'. Нажмите 'Завершить отслеживание', когда закончите."
    )
    await state.set_state(TrackActivityState.tracking)
    await track_time(activity_name, message, state)


async def track_time(activity_name: str, message: Message, state: FSMContext):
    start_time = time.time()
    await state.update_data(start_time=start_time, activity_name=activity_name)
    await message.answer(
        f"Отслеживание активности '{activity_name}' началось. Нажмите 'Завершить отслеживание', когда закончите.",
        reply_markup=kb.stop_tracking,
    )


@router.callback_query(F.data == "stop_tracking")
async def stop_tracking(callback: CallbackQuery, state: FSMContext):
    end_time = time.time()
    data = await state.get_data()
    start_time = data["start_time"]
    activity_name = data["activity_name"]
    duration = end_time - start_time

    user_tg_id = callback.from_user.id
    async with async_session as session:
        await track_activity(user_tg_id, activity_name, duration, session)

    await callback.message.answer(
        f"Отслеживание активности '{activity_name}' завершено. Продолжительность: {duration:.2f} секунд."
    )
    await state.clear()


@router.message(F.text == "Просмотр ваших активностей")
async def ask_for_date_to_view_activities(message: Message, state: FSMContext):
    await message.answer("Введите дату для просмотра активностей в формате ГГГГ-ММ-ДД:")
    await state.set_state(TrackActivityState.date)


async def view_activities(message: Message, entry_date: date):
    user_tg_id = message.from_user.id
    activities = await get_activities(user_tg_id, entry_date)
    if activities:
        response = "\n".join([f"{activity.activity_name}: {activity.duration} часов" for activity in activities])
        await message.answer(f"Ваши активности за {entry_date}: {response}")
    else:
        await message.answer("Активностей за эту дату нет.")


@router.message
async def process_date_for_activities(message: Message):
    try:
        entry_date = date.fromisoformat(message.text)
        await view_activities(message, entry_date)
    except ValueError:
        await message.answer("Некорректный формат даты. Пожалуйста, введите дату в формате ГГГГ-ММ-ДД.")
