from typing import Callable

from domain.exceptions import UserAlreadyExists
from domain.users import User
from repositories.base.users_base_repository import BaseAsyncUserRepository, BaseSyncUserRepository


class SyncUserCreateUseCase:
    """Sync create user use case"""
    def __init__(
            self,
            user_repo: BaseSyncUserRepository,
            hash_function: Callable,
        ) -> None:
        self.user_repo = user_repo
        self.hash_function = hash_function

    def execute(
            self,
            name: str,
            email: str,
            phone: str,
            password: str,
            is_admin: bool = False,
        ) -> User:
        existing_user = self.user_repo.get_by_email(email=email)
        if existing_user:
            raise UserAlreadyExists(f'User with email {email} already exists')

        hashed_password: str = self.hash_function(password)

        new_user: User = User(
            name=name,
            email=email,
            phone=phone,
            password=hashed_password,
            is_admin=is_admin,
        )
        self.user_repo.create(user=new_user)

        return new_user

class AsyncUserCreateUseCase:
    """Async create user use case"""
    def __init__(
            self,
            user_repo: BaseAsyncUserRepository,
            hash_function: Callable,
        ) -> None:
        self.user_repo = user_repo
        self.hash_function = hash_function

    async def execute(
            self,
            name: str,
            email: str,
            phone: str,
            password: str,
            is_admin: bool,
        ) -> User:
        existing_user = await self.user_repo.get_by_email(email=email)
        if existing_user:
            raise UserAlreadyExists(f'User with email {email} already exists')

        hashed_password: str = self.hash_function(password)

        new_user: User = User(
            name=name,
            email=email,
            phone=phone,
            password=hashed_password,
            is_admin=is_admin,
        )
        new_user: User = await self.user_repo.create(user=new_user)

        return new_user
