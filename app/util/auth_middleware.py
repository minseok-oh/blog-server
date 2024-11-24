from http.client import HTTPException
from typing import Optional

from requests import Request

from app.util.session_store import SessionStore
from main import app


@app.middleware('http')
async def auth_middleware(request: Request, call_next):
    exempt_paths = ["/api/auth/sign-up", "/api/auth/sign-in"]
    if request.url.path in exempt_paths:
        return await call_next(request)

    session_id = request.cookies.get("sid")
    if not session_id:
        raise HTTPException(status_code=401, detail="Unauthorized: Missing session ID")

    user = verify_session(session_id)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid session ID")

    request.state.user = user
    return await call_next(request)


def verify_session(session_id: str) -> Optional[dict]:
    session = SessionStore.get(session_id)
    if not session:
        return None
    return {"userId": session.userId, "role": session.role}
