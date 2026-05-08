from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from src.dbmodel import Setting

engine=create_async_engine(Setting().db_url,
                           pool_size=5,
                           max_overflow=10,
                           pool_timeout=30,
                           pool_recycle=1800,
                           echo=False
                           )
Base=declarative_base()
localsession=sessionmaker(bind=engine,class_=AsyncSession,expire_on_commit=False)
async def get_db():
    db=localsession()
    try:
        yield db
    finally:
        await db.close()