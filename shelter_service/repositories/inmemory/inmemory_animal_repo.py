from typing import Any
from domain.animals import Animal, Image
from repositories.base.animals_base_repository import BaseSyncAnimalRepository


class InMemoryAnimalRepo(BaseSyncAnimalRepository):
    def __init__(self, db_list: list, base_images_path: str) -> None:
        self._db_list = db_list

    def create(self, animal: Animal) -> Animal:
        animal.id = self._generate_animal_id()
        image_id: int = self._get_last_image_id() + 1
        for image in animal.images:
            image.id = image_id
            image_id += 1
            image.generate_relative_path(
                prefix=base_images_path,
                )
        self._db_list.append(animal.to_dict())
        return animal

    def _generate_animal_id(self) -> int:
        if not self._db_list:
            return 1
        return max([user.get('id', 0) for user in self._db_list]) + 1

    def _get_last_image_id(self) -> int:
        images_ids: set[int] = {image.id for animal in self._db_list for image in animal.images}
        max_id: int = max(images_ids)
        return max_id

    def __len__(self):
        return len(self._db_list)
