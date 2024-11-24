from fastapi import FastAPI

from app.routers.router import router
from app.util.auth_middleware import auth_middleware
from databases import init_db

app = FastAPI()

app.include_router(router)
app.middleware("http")(auth_middleware)

init_db()
