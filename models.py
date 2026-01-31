from db import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String
from pydantic import EmailStr


class Blogs(Base):
    __tablename__ = "blogs"
    blog_id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True, index=True
    )
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[EmailStr] = mapped_column(String(20), nullable=False)
    password: Mapped[str] = mapped_column(String(20), nullable=False)
    blog: Mapped[str] = mapped_column(String(100),nullable=True)
    slug: Mapped[str] = mapped_column(String(100),nullable=True)
