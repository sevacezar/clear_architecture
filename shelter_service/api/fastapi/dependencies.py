from repositories.postgres.settings import async_session

async def get_async_session():
    async with async_session() as session:
        yield session
