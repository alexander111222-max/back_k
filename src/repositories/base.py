from pydantic import BaseModel
from sqlalchemy import update, select

from src.api.dependencies import SessionDep
from src.utils.database import Base


class BaseRepository:


    def __init__(self, session: SessionDep, model):
        self._session = session
        self._model = model



    async def get_all(self):
        stmt = select(self._model)
        result = await self._session.execute(stmt)
        return result.scalars().all()


    async def get_paginated(self, page: int, per_page: int):
        stmt = select(self._model).limit(per_page).offset((page-1)*per_page)
        result = await self._session.execute(stmt)
        return result.scalars().all()


    async def edit(self, *filters, **data):

        stmt = (update(self._model)
                .where(*filters)
                .values(**data))

        await self._session.execute(stmt)



