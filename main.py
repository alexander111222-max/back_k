from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
from src.utils.database import init_database

from src.api.hotels import router





@asynccontextmanager
async def lifespan(app: FastAPI):

    await init_database()

    yield





app = FastAPI(lifespan=lifespan)

app.include_router(router)



def main():
    uvicorn.run(app)

if __name__ == "__main__":
    main()