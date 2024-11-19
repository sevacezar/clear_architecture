from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from config import config

DB_URL: str = config.postgres_url

engine = create_async_engine(
    url=DB_URL,
    echo=True,
)
async_session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)
