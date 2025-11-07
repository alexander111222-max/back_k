from pydantic import BaseModel

from src.services.base import BaseService


class HotelsService(BaseService):
    def __init__(self, repository, schema):
        super().__init__(repository, schema)


    async def edit_hotel(self, data: BaseModel, exclude_unset: bool = False, *filters):
        await self.edit(exclude_unset, data, *filters,)
