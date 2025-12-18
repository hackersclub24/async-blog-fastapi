from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from fastapi import Depends
from db import get_db

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}
# This is for cheeking that db is connected  or not 
@app.get("/db-check")
async def db_check(session: AsyncSession = Depends(get_db)):
    result = await session.execute(text("SELECT 1"))
    return {"db": "connected", "result": result.scalar()}