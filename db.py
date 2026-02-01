from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine,async_sessionmaker,AsyncSession
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql+asyncpg://postgres:admin123@localhost:5432/fastapi_db"

engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=True, future=True)

session = async_sessionmaker(
    engine , class_= AsyncSession,expire_on_commit=True
)

Base = declarative_base()
# hello
async def get_db():
    async with session() as s:
        print("opening session")
        yield s
        print("closed session")    
