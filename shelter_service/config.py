from dataclasses import dataclass
from environs import Env

@dataclass
class DBConfig:
    username: str
    password: str
    host: str
    port: int
    db_name: str

def get_db_config() -> DBConfig:
    pass

db_config: DBConfig = get_db_config()