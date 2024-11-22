from fastapi import APIRouter

from app.routers import auth_routers

router = APIRouter()

router.include_router(auth_routers.router)
