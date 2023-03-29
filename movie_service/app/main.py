from fastapi import FastAPI
from app.api.movies import router
from app.api.db import metadata, database, engine


# app = FastAPI()
app = FastAPI(openapi_url="/api/v1/movies/openapi.json", docs_url="/api/v1/movies/docs")
app.include_router(router, prefix='/api/v1/movies', tags=['movies'])


metadata.create_all(engine)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
