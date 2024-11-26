from typing import Any
from domain.animals import Animal, Image
from repositories.base.animals_base_repository import BaseSyncAnimalRepository


class InMemoryAnimalRepo(BaseSyncAnimalRepository):
    def __init__(self, db_list: list, base_images_path: str) -> None:
        self._db_list = db_list
        self._base_images_path = base_images_path

    def create(self, animal: Animal) -> Animal:
        animal.id = self._generate_animal_id()
        image_id: int = self._get_last_image_id() + 1
        for image in animal.images:
            image.id = image_id
            image_id += 1
            image.generate_relative_path(
                prefix=self._base_images_path,
                )
        self._db_list.append(animal.to_dict())
        return animal

    def _generate_animal_id(self) -> int:
        if not self._db_list:
            return 1
        return max([user.get('id', 0) for user in self._db_list]) + 1

    def _get_last_image_id(self) -> int:
        images_ids: set[int] = {image.get('id') for animal in self._db_list for image in animal.get('images')}
        max_id: int = max(images_ids)
        return max_id

    def __len__(self):
        return len(self._db_list)

    def get_by_id(self, id: int) -> Animal | None:
        animals: list[Any] = list(filter(lambda x: x.get('id') == id, self._db_list))
        if not animals:
            return None
        animal_obj: Animal = Animal.from_dict(animal_dict=animals[0])
        return animal_obj

    def get_all(self, offset: int = 0, limit: int | None = None) -> list[Any]:
        animals: list[Any] = self._db_list[offset:]
        if limit:
            animals = animals[:limit]
        return [Animal.from_dict(i_animal) for i_animal in animals]

    def get_filtered(self, filters: dict[str, Any]) -> list[Any]:
        animals_filtred: list[Any] = list(filter(
            lambda x: all([getattr(x, i_attr) == i_value for i_attr, i_value in filters.items()]),
            self._db_list,
        ))
        return [Animal.from_dict(animal) for animal in animals_filtred]

    def delete(self, id: int) -> None:
        if not self._db_list:
            return None
        self._db_list = [animal for animal in self._db_list if animal.get('id') != id]

    def update_by_id(self, id: int, params: dict[str, Any]) -> Animal | None:
        animal_obj: Animal = self.get_by_id(id=id)
        if not animal_obj:
            return None
        for attr, value in params.items():
            if hasattr(self, attr):
                self.__setattr__(attr, value)
        return animal_obj
