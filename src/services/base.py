from pydantic import BaseModel


class BaseService:

    def __init__(self, repository, schemas):
        self._repository = repository
        self._schemas = schemas


    async def edit(self, data: BaseModel, exclude_unset: bool = False, *filters):
        data = data.model_dump(exclude_unset=exclude_unset)
        await self._repository.edit(*filters, **data)


    async def get_paginated(self, page: int, per_page: int):
        objs = await self._repository.get_paginated(page, per_page)
        return objs

