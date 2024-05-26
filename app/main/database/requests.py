from sqlalchemy.future import select
import datetime
from .models import User, DiaryEntry, ActivityTracking
from .db import async_session, AsyncSession

async def add_diary_entry(user_tg_id: int, entry_date: datetime.date, content: str):
    async with async_session as session:
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

async def get_diary_entries(user_tg_id: int, entry_date: datetime.date):
    async with async_session as session:
        result = await session.execute(
            select(DiaryEntry).join(User).where(User.tg_id == user_tg_id, DiaryEntry.date == entry_date)
        )
        entries = result.scalars().all()

        return entries

import datetime

async def track_activity(user_id: int, activity_name: str, duration: float, session: AsyncSession):
    async with session.begin():
        today = datetime.date.today()
        activity = ActivityTracking(user_id=user_id, activity_name=activity_name, duration=duration, date=today)
        session.add(activity)

async def get_activities(user_tg_id: int, entry_date: datetime.date):
    async with async_session as session:
        result = await session.execute(
            select(ActivityTracking).join(User).where(User.tg_id == user_tg_id, ActivityTracking.date == entry_date)
        )
        activities = result.scalars().all()

        return activities
