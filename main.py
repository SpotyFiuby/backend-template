import os
from dotenv import load_dotenv
from fastapi import FastAPI
from app.api.api import api_router
from fastapi_sqlalchemy import DBSessionMiddleware

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
app.include_router(api_router)
