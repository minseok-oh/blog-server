from fastapi import FastAPI

from app.routers.router import router
from databases import init_db

app = FastAPI()

app.include_router(router)
app.middleware('http')

init_db()
