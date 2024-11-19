from typing import Any
from config import DBConfig
from repositories.base.users_base_repository import BaseAsyncUserRepository, BaseSyncUserRepository
from repositories.inmemory.inmemory_repo import InMemoryUserRepo
from repositories.postgres.postgres_repo import PostgresUserRepo
# mongoDB

class RepositoryFactory:
    """Class for creating repository realizations"""

    def __init__(self, db_config: DBConfig) -> None:
        self._db_config = db_config

    def get_user_repository(self,
                            in_memory_db: list[dict] | None = None,
                            sql_session: Any = None,
                            mongodb_collection: Any = None,
        ) -> BaseAsyncUserRepository | BaseSyncUserRepository:

        if self._db_config.is_inmemory:
            return InMemoryUserRepo(db_list=in_memory_db)
        if self._db_config.is_postgres:
            if not sql_session:
                raise AttributeError('Missing "sql_session" argument')
            if self._db_config.is_async:
                return PostgresUserRepo(session=sql_session)
            else:
                raise Exception('Sync postgres repository is not defiened')
        if self._db_config.is_mongodb:
            pass

    def get_animal_repository():
        pass