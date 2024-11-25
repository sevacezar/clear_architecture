from dataclasses import dataclass, asdict, fields
from datetime import datetime

@dataclass
class User:
    name: str
    email: str
    phone: str
    password: str
    is_admin: bool = False
    created_at: datetime = datetime.now()
    id: int | None = None


    @classmethod
    def from_dict(cls, user_dict: dict):
        return cls(**user_dict)

    def to_dict(self):
        return asdict(self)

    def update(self, params: dict) -> 'User':
        field_names: set = {field.name for field in fields(self)}
        for attr, value in params.items():
            if attr in field_names:
                self.__setattr__(attr, value)
        return self

    def __bool__(self):
        return True

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return all((
            self.id == other.id,
            self.name == other.name,
            self.email == other.email,
            self.phone == other.phone,
            self.password == other.password,
            self.is_admin == other.is_admin,
            self.created_at == other.created_at,
        ))

    #TODO: Validation!!!