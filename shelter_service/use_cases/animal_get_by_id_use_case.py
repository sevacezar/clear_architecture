from domain.animals import Animal
from repositories.base.animals_base_repository import BaseSyncAnimalRepository

class SyncAnimalGetByIdUseCase:
    def __init__(self, animal_repo: BaseSyncAnimalRepository):
        self.repo = animal_repo

    def execute(self, id: int) -> Animal | None:
        animal: Animal | None = self.repo.get_by_id(id=id)
        return animal
    