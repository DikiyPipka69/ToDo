# импортируем асинхронный движок и фабрику сессий
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
# DeclarativeBase базовый класс для моделей, Mapped и mapped_column - современные способы описания колонок
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


engine = create_async_engine('sqlite+aiosqlite:///todo.db')

new_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session():
    async with new_session() as session:
        yield session

