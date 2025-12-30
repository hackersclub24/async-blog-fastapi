from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from fastapi import Depends
from db import get_db
from models import User 
from sqlalchemy import select, and_
from typing import List, Optional
from routers import app_router

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}
# This is for cheeking that db is connected  or not 
@app.get("/db-check")
async def db_check(session: AsyncSession = Depends(get_db)):
    result = await session.execute(text("SELECT 1"))
    return {"db": "connected", "result": result.scalar()}
@app.get("/chek-user")
async def check(db: AsyncSession = Depends(get_db)):
    stmt = select(User)
    results = await db.execute(stmt)
    return results.scalar()


app.include_router(app_router)