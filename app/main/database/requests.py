from sqlalchemy.future import select
from datetime import date
from .models import User, DiaryEntry
from .db import async_session


async def add_diary_entry(user_tg_id: int, entry_date: date, content: str):
    async with async_session as session:  # Уберите вызов функции async_session()
        result = await session.execute(
            select(User).where(User.tg_id == user_tg_id)
        )
        user = result.scalars().first()

        if not user:
            user = User(tg_id=user_tg_id)
            session.add(user)
            await session.commit()
            await session.refresh(user)

        new_entry = DiaryEntry(user_id=user.id, date=entry_date, content=content)
        session.add(new_entry)
        await session.commit()

async def get_diary_entries(user_tg_id: int, entry_date: date):
    async with async_session as session:
        result = await session.execute(
            select(DiaryEntry).join(User).where(User.tg_id == user_tg_id, DiaryEntry.date == entry_date)
        )
        entries = result.scalars().all()

        # Отладочный вывод для проверки результатов запроса
        print("Запрос:", result)
        print("Найденные записи:", entries)

        return entries