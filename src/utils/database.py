from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

engine = create_async_engine("postgresql+asyncpg://postgres:example@localhost:5432/backendKurs")

def get_async_session():
    async_session = async_sessionmaker(engine)
    return async_session

async def init_database():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)




