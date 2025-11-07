from pydantic import BaseModel


class HotelPatchSchema(BaseModel):
    title: str | None = None
    name: str| None = None
    location: str | None = None

class HotelPutSchema(BaseModel):
    title: str
    name: str
    location: str
