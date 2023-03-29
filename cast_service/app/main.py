from fastapi import FastAPI
from app.api.casts import router
from app.api.db import metadata, database, engine


# app = FastAPI()
app = FastAPI(openapi_url="/api/v1/casts/openapi.json", docs_url="/api/v1/casts/docs")
app.include_router(router, prefix='/api/v1/casts', tags=['casts'])


metadata.create_all(engine)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
