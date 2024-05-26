from app.main.database.models import Base

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async_session = AsyncSessionLocal()

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)