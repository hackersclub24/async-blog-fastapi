from fastapi import FastAPI, Depends, Response, Request, Cookie
from contextlib import asynccontextmanager
from db import engine, Base, get_db
from models import Blogs
from typing import List, Optional
from schemas import Create_blog, Signup, login,login2
from sqlalchemy.ext.asyncio import AsyncSession
import jwt
from sqlalchemy import select,and_


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        res = await conn.run_sync(
            lambda s: engine.dialect.has_table(s, Blogs.__tablename__)
        )
        if not res:
            await conn.run_sync(Base.metadata.create_all)
    yield


def create_token(login: login,data2 : dict, response: Response, db: AsyncSession = Depends(get_db)):
    print(data2["blog_id"])
    data = {"email": login.email, "id": data2["blog_id"]}
    encoded_jwt = jwt.encode(data, "secret", algorithm="HS256")
    response.set_cookie("access_token", data, max_age=10000)
    return data


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def welcome():
    return {"data": "done"}


@app.post("/create-blog")
async def create_blog(create_blog: Create_blog, db: AsyncSession = Depends(get_db)):
    new_blog = Blogs(
        name=create_blog.name,
        email=create_blog.email,
        password=create_blog.password,
        blog=create_blog.blog,
        slug=create_blog.slug,
    )
    db.add(new_blog)
    await db.commit()
    await db.refresh(new_blog)
    return new_blog


@app.post("/signin")
async def signin(signup: Signup, db: AsyncSession = Depends(get_db)):
    new_user = Blogs(
        name=signup.name,
        email=signup.email,
        password=signup.password,
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


@app.post("/login")
async def login(login: login, db: AsyncSession = Depends(get_db)):
    stmt = select(Blogs).where(
        login.email == Blogs.email and login.password == Blogs.password
    )
    result = await db.execute(stmt)
    # data  = result.scalars().all()
    data  = result.scalar_one()
    dict_data = data.__dict__
    
    if data:
        token = create_token(login=login,data2=dict_data,response=Response)
        return token
    return data