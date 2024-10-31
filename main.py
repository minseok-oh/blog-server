from fastapi import FastAPI

from databases import init_db

app = FastAPI()

init_db()
