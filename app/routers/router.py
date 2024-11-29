from fastapi import APIRouter

from app.routers import auth_routers, post_routers, comment_routers, schedule_routers

router = APIRouter()

router.include_router(auth_routers.router)
router.include_router(post_routers.router)
router.include_router(comment_routers.router)
router.include_router(schedule_routers.router)
