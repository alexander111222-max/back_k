
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.database import get_async_session


async def get_session():
    async_sess = get_async_session()

    async with async_sess() as session:
        yield session
        await session.commit()


SessionDep = Annotated[AsyncSession, Depends(get_session)]