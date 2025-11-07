from fastapi import APIRouter

from src.api.dependencies import SessionDep
from src.models.hotels import HotelsOrm
from src.repositories.hotels import HotelsRepository
from src.schemas.hotels import HotelPutSchema, HotelPatchSchema, BaseHotelsSchema
from src.services.hotels import HotelsService

router = APIRouter()



@router.put("/hotels/{hotel_id}")
async def partial_update(session: SessionDep, hotel_id: int, data: HotelPutSchema):
    await (HotelsService(HotelsRepository(session), HotelPutSchema)
           .edit_hotel(False, data, (HotelsOrm.id == hotel_id)))

@router.patch("/hotels/{hotel_id}")
async def full_update(session: SessionDep, hotel_id: int, data: HotelPatchSchema):
    await (HotelsService(HotelsRepository(session), HotelPatchSchema)
           .edit_hotel(True, data, (HotelsOrm.id == hotel_id)))






@router.get("/hotels/get_page")
async def get_hotels_page(session: SessionDep,
                          page: int | None = 1,
                          per_page: int | None = 3):
    hotels = await HotelsService(HotelsRepository(session), BaseHotelsSchema).get_paginated(page, per_page)
    return hotels
