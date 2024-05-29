from sqlalchemy.future import select
from datetime import date
from .models import User, DiaryEntry, ActivityTracking, Reminder
from .db import async_session, AsyncSession
import datetime


async def add_diary_entry(user_tg_id: int, entry_date: date, content: str):
    async with async_session as session:
        result = await session.execute(select(User).where(User.tg_id == user_tg_id))
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
        return entries


async def track_activity(user_tg_id: int, activity_name: str, duration: float, session: AsyncSession):
    async with session.begin():
        result = await session.execute(select(User).where(User.tg_id == user_tg_id))
        user = result.scalars().first()

        if not user:
            user = User(tg_id=user_tg_id)
            session.add(user)
            await session.commit()
            await session.refresh(user)

        activity = ActivityTracking(user_id=user.id, activity_name=activity_name, duration=duration, date=date.today())
        session.add(activity)


async def get_activities(user_tg_id: int, entry_date: date):
    async with async_session as session:
        result = await session.execute(
            select(ActivityTracking).join(User).where(User.tg_id == user_tg_id, ActivityTracking.date == entry_date)
        )
        activities = result.scalars().all()
        return activities


async def add_reminder(user_tg_id: int, message: str, reminder_time: str):
    async with async_session as session:
        result = await session.execute(select(User).where(User.tg_id == user_tg_id))
        user = result.scalars().first()

        if not user:
            user = User(tg_id=user_tg_id)
            session.add(user)
            await session.commit()
            await session.refresh(user)

        # Преобразуем время напоминания из строки в объект time
        reminder_time_obj = datetime.strptime(reminder_time, '%H:%M').time()

        new_reminder = Reminder(user_id=user.id, message=message, reminder_time=reminder_time_obj)
        session.add(new_reminder)
        await session.commit()


async def get_reminders(user_tg_id: int):
    async with async_session as session:
        result = await session.execute(
            select(Reminder).join(User).where(User.tg_id == user_tg_id)
        )
        reminders = result.scalars().all()
        return reminders


async def delete_reminder(reminder_id: int):
    async with async_session as session:
        result = await session.execute(select(Reminder).where(Reminder.id == reminder_id))
        reminder = result.scalars().first()

        if reminder:
            await session.delete(reminder)
            await session.commit()