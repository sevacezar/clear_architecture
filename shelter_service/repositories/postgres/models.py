from datetime import datetime

from sqlalchemy.dialects.postgresql import ENUM as PgEnum
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy.sql import func

from domain.animals import AnimalType, AnimalGender, CoatType, Status
from domain.users import User

Base = declarative_base()

class UserSQLModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True, index=True)
    phone: Mapped[str]
    password: Mapped[str] = mapped_column(nullable=False)
    is_admin: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    def to_dict(self) -> User:
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'is_admin': self.is_admin,
            'created_at': self.created_at,
        }

class AnimalSQLModel(Base):
    __tablename__ = 'animals'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(
        PgEnum(AnimalType, name='animal_types_enum', create_type=False),
        nullable=False,
        default=AnimalType.dog,
    )
    gender: Mapped[str] = mapped_column(
        PgEnum(AnimalGender, name='animal_genders_enum', create_type=False),
        nullable=False,
        default=AnimalGender.male,
    )
    color: Mapped[str] = mapped_column(nullable=False)
    weight: Mapped[int] = mapped_column(nullable=False)
    breed: Mapped[str] = mapped_column(nullable=False, default='mixed_breed')
    coat: Mapped[str] = mapped_column(
        PgEnum(CoatType, name='animal_coats_enum', create_type=False),
        nullable=False,
        default=CoatType.medium,
    )
    birth_date: Mapped[datetime]
    in_shelter_at: Mapped[datetime] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(
        PgEnum(Status, name='animal_status_enum', create_type=False),
        nullable=False,
        default=Status.available,
    )
    ok_with_children: Mapped[bool] = mapped_column(default=True)
    ok_with_cats: Mapped[bool] = mapped_column(default=True)
    ok_with_dogs: Mapped[bool] = mapped_column(default=True)
    has_vaccinations: Mapped[bool] = mapped_column(default=True)
    is_sterilized: Mapped[bool] = mapped_column(default=True)
    description: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(onupdate=func.now())
