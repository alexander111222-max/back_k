from pydantic import BaseModel
from sqlalchemy import update

from src.api.dependencies import SessionDep
from src.utils.database import Base


class BaseRepository:


    def __init__(self, session: SessionDep, model):
        self._session = session
        self._model = model


    async def edit(self, *filters, **data):

        stmt = (update(self._model)
                .where(*filters)
                .values(**data))

        await self._session.execute(stmt)



