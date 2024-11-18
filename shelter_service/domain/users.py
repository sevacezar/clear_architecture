from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class User:
    id: int | None
    name: str
    email: str
    phone: str
    password: str
    is_admin: bool
    created_at: datetime = datetime.now()

    @classmethod
    def from_dict(cls, user_dict: dict):
        return cls(**user_dict)

    def to_dict(self):
        return asdict(self)

    def update(self, params: dict) -> 'User':
        for attr, value in params.items():
            if hasattr(self, attr):
                setattr(
                    obj=self,
                    name=attr,
                    value=value,
                )
        return self

    #TODO: Validation!!!