from datetime import datetime, timezone

from domain.animals import Animal, Image, CoatType, AnimalGender, AnimalType, Status
from domain.users import User
from repositories.base.animals_base_repository import BaseSyncAnimalRepository
from repositories.base.users_base_repository import BaseSyncUserRepository

class SyncAnimalCreateUseCase:
    """Sync create animal use case"""
    def __init__(
            self,
            user_repo: BaseSyncUserRepository,
            animal_repo: BaseSyncAnimalRepository,
        ):
        self.user_repo = user_repo
        self.animal_repo = animal_repo

    def execute(
            self,
            user_id: int,
            name: str,
            color: str,
            weight: int,
            birth_date: datetime,
            in_shelter_at: datetime,
            updated_at: datetime,
            description: str,
            breed: str = 'breedless',
            coat: CoatType = CoatType.medium.value,
            type: AnimalType = AnimalType.dog.value,
            gender: AnimalGender = AnimalGender.male.value,
            status: Status = Status.available.value,
            ok_with_children: bool = True,
            ok_with_cats: bool = True,
            ok_with_dogs: bool = True,
            has_vaccinations: bool = True,
            is_sterilized: bool = True,
            created_at: datetime = datetime.now(tz=timezone.utc),
            id: int | None = None,
            images: list[Image] = [],
    ):
        user: User = self.user_repo.get_by_id(id=user_id)
        if not user or not user.is_admin:
            raise PermissionError('Only admins can create animals')

        animal: Animal = Animal(
            name=name,
            color=color,
            weight=weight,
            birth_date=birth_date,
            in_shelter_at=in_shelter_at,
            updated_at=updated_at,
            description=description,
            breed=breed,
            coat=coat,
            type=type,
            gender=gender,
            status=status,
            ok_with_children=ok_with_children,
            ok_with_cats=ok_with_cats,
            ok_with_dogs=ok_with_dogs,
            has_vaccinations=has_vaccinations,
            is_sterilized=is_sterilized,
            created_at=created_at,
            id=id,
            images=images,
        )
        return self.animal_repo.create(animal=animal)
