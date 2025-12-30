from fastapi import APIRouter, Depends, HTTPException, Response
from db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from models import User
from sqlalchemy import select, and_
from typing import List, Optional
# from schemas import UserBase, UserRead


app = APIRouter(prefix="/user", tags=["users"])

@app.get("/chek-user")
async def check(db: AsyncSession = Depends(get_db)):
    stmt = select(User)
    results = await db.execute(stmt)
    return results.scalar()