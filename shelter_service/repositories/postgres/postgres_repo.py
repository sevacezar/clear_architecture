from typing import Any
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.users import User
from repositories.base.users_base_repository import BaseAsyncUserRepository
from repositories.postgres.models import UserSQLModel

class PostgresUserRepo(BaseAsyncUserRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, user: User) -> User:
        user_orm: UserSQLModel = UserSQLModel(
            name=user.name,
            email=user.email,
            phone=user.phone,
            password=user.password,
            is_admin=user.is_admin,
        )
        self._session.add(user)
        await self._session.commit()
        return user.update({'id': user_orm.id, 'created_at': user_orm.created_at})

    async def get_by_email(self, email: str) -> User | None:
        query = select(UserSQLModel).where(UserSQLModel.email == email)
        res = await self._session.execute(query)
        user_orm: UserSQLModel | None = res.scalar_one_or_none()
        if user_orm is None:
            return None
        return User.from_dict(user_dict=user_orm.to_dict())

    async def get_all(self, offset: int = 0, limit: int | None = None) -> list[Any]:
        query = select(UserSQLModel).offset(offset)
        if limit:
            query = query.limit(limit)
        res = await self._session.execute(query)
        users_orm: list[Any] = res.scalars().all()
        if not users_orm:
            return []
        users: list[User] = [User.from_dict(user_orm.to_dict()) for user_orm in users_orm]
        return users

    async def get_filtered(self, filters: dict[str, Any]) -> list[Any]:
        query = select(UserSQLModel)
        for field, value in filters.items():
            query = query.filter(getattr(UserSQLModel, field) == value)
        res = await self._session.execute(query)
        users_orm: list[Any] = res.scalars().all()
        if not users_orm:
            return []
        users: list[User] = [User.from_dict(user_orm.to_dict()) for user_orm in users_orm]
        return users

    async def delete(self, id: int) -> None:
        query = select(UserSQLModel).where(UserSQLModel.id == id)
        res = await self._session.execute(query)
        user_orm: UserSQLModel | None = res.scalar_one_or_none()
        if user_orm:
            await self._session.delete(user_orm)
            await self._session.commit()
