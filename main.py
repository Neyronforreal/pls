from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel

from service.service_api import toy_router
from user.user_api import user_router

from database import Base, engine


app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(toy_router)

app.get('/test')


async def test():
    return 'Test page'
