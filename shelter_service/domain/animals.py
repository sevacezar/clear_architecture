from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum

class AnimalType(Enum):
    cat: str = 'cat'
    dog: str = 'dog'


class AnimalGender(Enum):
    male: str = 'male'
    female: str = 'female'


class CoatType(Enum):
    short: str = 'short'
    medium: str = 'medium'
    long: str = 'long'


class Status(Enum):
    available: str = 'available_for_adoption'
    family: str = 'in_the_family'
    reserve: str = 'reserve'


@dataclass
class Animal:
    id: int | None
    name: str
    type: AnimalType
    gender: AnimalGender
    color: str
    weight: int
    breed: str
    coat: CoatType
    birth_date: datetime
    in_shelter_at: datetime
    created_at: datetime
    status: Status
    ok_with_children: bool
    ok_with_cats: bool
    ok_with_dogs: bool
    has_vaccinations: bool
    is_sterilized: bool
    description: str

    @classmethod
    def from_dict(cls, animal_dict: dict) -> 'Animal':
        return cls(**animal_dict)

    def to_dict(self):
        return asdict(self)
