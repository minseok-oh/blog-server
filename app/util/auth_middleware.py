from typing import Optional

from fastapi import Request, HTTPException, Response

from app.util.session_store import SessionStore


async def auth_middleware(request: Request, call_next):
    if request.method == "OPTIONS":
        return Response(status_code=200)

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
    return {"user_id": session.user_id, "username": session.username, "role": session.role}
