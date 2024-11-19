from typing import Any
from clear_architecture.shelter_service.domain.users import User
from repositories.base.users_base_repository import BaseSyncUserRepository

class InMemoryUserRepo(BaseSyncUserRepository):
    def __init__(self, db_list: list) -> None:
        self._db_list = db_list

    def create(self, user: User) -> User:
        user.id = self._generate_id()
        self._db_list.append(user.to_dict())
        return user

    def get_by_email(self, email: str) -> User | None:
        users: list[Any] = list(filter(lambda x: x.get('email') == email, self._db_list))
        if not users:
            return None
        user_obj: User = User.from_dict(users[0])
        return user_obj

    def get_all(self, offset: int = 0, limit: int | None = None) -> list[Any]:
        users: list[Any] = self._db_list[offset]
        if limit:
            users = users[:offset+limit]
        return [User.from_dict(i_user) for i_user in self._db_list]

    def get_filtered(self, filters: dict[str, Any]) -> list[Any]:
        users_filtred: list[Any] = list(filter(
            lambda x: all([getattr(x, i_attr) == i_value for i_attr, i_value in filters.items()]),
            self._db_list,
        ))
        return [User.from_dict(user) for user in users_filtred]

    def delete(self, id: int) -> None:
        if not self._db_list:
            return None
        self._db_list = [user for user in self._db_list if user.get('id') != id]

    def _generate_id(self):
        if not self._db_list:
            return 1
        return max([user.get('id', 0) for user in self._db_list]) + 1
    