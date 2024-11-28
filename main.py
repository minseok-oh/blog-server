from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.router import router
from app.util.auth_middleware import auth_middleware
from databases import init_db

app = FastAPI()

app.include_router(router)
app.middleware("http")(auth_middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()
