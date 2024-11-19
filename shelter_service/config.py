import os
from dotenv import load_dotenv


class DBConfig:
    def __init__(self) -> None:
        self.db_type: str = os.getenv('DB_TYPE', 'inmemory')
        self.app_mode: str = os.getenv('APP_MODE', 'sync')

        if self.is_postgres:
            self.username: str = os.getenv('POSTGRES_USERNAME', 'postgres')
            self.password: str = os.getenv('POSTGRES_PASSWORD', 'postgres')
            self.host: str = os.getenv('POSTGRES_HOST', 'localhost')
            self.port: int = int(os.getenv('POSTGRES_PORT', '5432'))
            self.db_name: str = os.getenv('POSTGRES_DBNAME', 'postgres')
        elif self.is_mongodb:
            self.host: str = os.getenv('MONGODB_HOST', 'localhost')
            self.port: int = int(os.getenv('MONGODB_PORT', '27017'))

    def is_postgres(self) -> bool:
        return self.db_type == 'postgres'

    def is_mongodb(self) -> bool:
        return self.db_type == 'mongodb'

    def is_inmemory(self) -> bool:
        return self.db_type == 'inmemory'

    def is_async(self) -> bool:
        return self.app_mode == 'async'

    def is_sync(self) -> bool:
        return self.app_mode == 'sync'

    @property
    def postgres_url(self) -> str | None:
        if not self.is_postgres:
            return None

        if self.app_mode == 'async':
            prefix: str = 'postgresql+asyncpg'
        else:
            prefix: str = 'postgresql+psycopg2'
        return '{prefix}://{username}:{password}@{host}:{port}/{db_name}'.format(
            prefix=prefix,
            username=self.username,
            password=self.password,
            host=self.host,
            port=self.port,
            db_name=self.db_name
        )

    @property
    def mongodb_url(self) -> str | None:
        if not self.is_mongodb:
            return None

        prefix: str = 'mongodb'
        return '{prefix}://{host}:{port}'.format(
            prefix=prefix,
            host=self.host,
            port=self.port,
        )


load_dotenv()
config = DBConfig()
