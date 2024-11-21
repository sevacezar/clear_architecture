

from typing import Any
from repositories.base.users_base_repository import BaseAsyncUserRepository, BaseSyncUserRepository

class SyncUsersGetAllUseCase:
    """Sync get all users use case"""
    def __init__(
            self,
            user_repo: BaseSyncUserRepository,
        ) -> None:
        self.user_repo = user_repo

    def execute(
            self,
            offset: int = 0,
            limit: int | None = None
        ) -> list[Any]:
        users: list[Any] = self.user_repo.get_all(
            offset=offset,
            limit=limit,
        )
        return users

class AsyncUsersGetAllUseCase:
    """Async get all users use case"""
    def __init__(
            self,
            user_repo: BaseSyncUserRepository,
        ) -> None:
        self.user_repo = user_repo

    async def execute(
            self,
            offset: int = 0,
            limit: int | None = None
        ) -> list[Any]:
        users: list[Any] = await self.user_repo.get_all(
            offset=offset,
            limit=limit,
        )
        return users