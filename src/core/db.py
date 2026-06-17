from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.models.categories import Category

# database_url = 'postgresql+asyncpg://postgres:postgres@localhost:55432/northwind'
database_url = 'postgresql+asyncpg://postgres:postgres@db:5432/northwind'
engine = create_async_engine(database_url, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():

    async with AsyncSessionLocal() as async_session:
        yield async_session


async def check_connection():
    async with AsyncSessionLocal() as async_session:
        try:
            result = await async_session.execute(select(Category))
            categories = result.scalars().all()
            for category in categories:
                print(f'{category.category_name}, {category.description[:10]}.')

        except Exception as e:
            print(f"Ошибка подключения: {e}")
