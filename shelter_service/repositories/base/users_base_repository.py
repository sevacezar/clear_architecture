from abc import abstractmethod, ABC
from typing import Any

from domain.users import User

class BaseSyncUserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> User:
        """Creates new user"""
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        """Gets user by email"""
        pass

    @abstractmethod
    def get_all(self, offset: int = 0, limit: int | None = None) -> list[Any]:
        """Gets all users with offset and limit"""
        pass

    @abstractmethod
    def get_filtered(self, filters: dict[str, Any]) -> list[Any]:
        """Gets users with filters"""
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        """Deletes user"""
        pass


class BaseAsyncUserRepository(ABC):
    @abstractmethod
    async def create(self, user: User) -> User:
        """Creates new user"""
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> User | None:
        """Gets user by id"""
        pass

    @abstractmethod
    async def get_all(self, offset: int = 0, limit: int | None = None) -> list[Any]:
        """Gets all users with offset and limit"""
        pass

    @abstractmethod
    async def get_filtered(self, filters: dict[str, Any]) -> list[Any]:
        """Gets users with filters"""
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        """Deletes user"""
        pass
