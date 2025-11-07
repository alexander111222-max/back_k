from src.api.dependencies import SessionDep
from src.models.hotels import HotelsOrm
from src.repositories.base import BaseRepository


class HotelsRepository(BaseRepository):

    def __init__(self, session: SessionDep):
        super().__init__(session, HotelsOrm)

