from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

wngine = create_async_engine('sqlite+aiosqlite:///books.db')