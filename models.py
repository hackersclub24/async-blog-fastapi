from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, String, DECIMAL, ForeignKey
from db import Base
from pydantic import EmailStr
from enum import Enum


class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True, index=True
    )