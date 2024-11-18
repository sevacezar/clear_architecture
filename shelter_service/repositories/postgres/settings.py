from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from config import db_config

DB_URL: str = 'postgresql+asyncpg://{username}:{password}@{host}:{port}/{db_name}'.format(
    username=db_config.username,
    password=db_config.password,
    host=db_config.host,
    port=db_config.port,
    db_name=db_config.db_name,
)

engine = create_async_engine(
    url=DB_URL,
    echo=True,
)
async_session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)
