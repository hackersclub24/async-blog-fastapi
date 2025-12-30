from fastapi import APIRouter, Depends, HTTPException, Response
from db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from models import Blog
from sqlalchemy import select, and_
from typing import List, Optional
# from schemas import UserBase, UserRead


app = APIRouter(prefix="/blogs", tags=["Blogs"])

@app.get("/show-blogs")
async def display(db: AsyncSession = Depends(get_db)):
    stmt = select(Blog)
    results = await db.execute(stmt)
    return results.scalar()