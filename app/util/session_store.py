class SessionStore:
    _store = {}

    @classmethod
    def save(cls, session_id: str, data: dict):
        cls._store[session_id] = data

    @classmethod
    def get(cls, session_id: str) -> dict:
        return cls._store.get(session_id)

    @classmethod
    def delete(cls, session_id: str):
        if session_id in cls._store:
            del cls._store[session_id]
