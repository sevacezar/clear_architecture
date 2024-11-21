from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

# from api.fastapi.dependencies import get_async_session
from api.fastapi.users.schemas import GetUserDTO, CreateUserDTO, GetMultipleUsersDTO
from config import config
from domain.users import User
from repositories.base.users_base_repository import BaseSyncUserRepository
from repositories.factory import RepositoryFactory
from use_cases.user_create_use_case import SyncUserCreateUseCase
from use_cases.users_get_all_use_case import SyncUsersGetAllUseCase
from utils.hash_password import get_password_hash

router = APIRouter(prefix='/users', tags=['Users'])

users_db: list[dict] = []  # In-memory data base initialization

@router.post(
    '/',
    response_model=GetUserDTO,
)
async def create_user(
    dto: CreateUserDTO,
    # session: AsyncSession = Depends(get_async_session),
):
    user_repo: BaseSyncUserRepository = RepositoryFactory(db_config=config).get_user_repository(in_memory_db=users_db)
    use_case: SyncUserCreateUseCase = SyncUserCreateUseCase(
        user_repo=user_repo,
        hash_function=get_password_hash,
    )
    user: User = use_case.execute(**dto.model_dump())
    return user.to_dict()

@router.get(
    '/',
    response_model=GetMultipleUsersDTO,
)
async def get_all_users(
    offset: int = 0,
    limit: int | None = None,
    # session: AsyncSession = Depends(get_async_session),
):
    user_repo: BaseSyncUserRepository = RepositoryFactory(db_config=config).get_user_repository(in_memory_db=users_db)
    use_case: SyncUsersGetAllUseCase = SyncUsersGetAllUseCase(
        user_repo=user_repo,
    )
    users: list[Any] = use_case.execute(offset=offset, limit=limit)
    return [user.to_dict() for user in users]
