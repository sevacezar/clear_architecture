from abc import abstractmethod, ABC
from typing import Any

from domain.animals import Animal

class BaseSyncAnimalRepository(ABC):
    @abstractmethod
    def create(self, animal: Animal) -> Animal:
        """Creates new animal"""
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Animal | None:
        """Gets animal by id"""
        pass

    @abstractmethod
    def get_all(self, offset: int = 0, limit: int | None = None) -> list[Any]:
        """Gets all animals with offset and limit"""
        pass

    @abstractmethod
    def get_filtered(self, filters: dict[str, Any]) -> list[Any]:
        """Gets animals with filters"""
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        """Deletes animal"""
        pass

    @abstractmethod
    def update_by_id(self, id: int, params: dict[str, Any]) -> Animal | None:
        """Updates animal"""
        pass


class BaseAsyncAnimalRepository(ABC):
    @abstractmethod
    async def create(self, animal: Animal) -> Animal:
        """Creates new animal"""
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> Animal | None:
        """Gets animal by id"""
        pass

    @abstractmethod
    async def get_all(self, offset: int = 0, limit: int | None = None) -> list[Any]:
        """Gets all animals with offset and limit"""
        pass

    @abstractmethod
    async def get_filtered(self, filters: dict[str, Any]) -> list[Any]:
        """Gets animals with filters"""
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        """Deletes animal"""
        pass

    @abstractmethod
    async def update_by_id(self, id: int, params: dict[str, Any]) -> Animal:
        """Updates animal"""
        pass
