from datetime import datetime, timedelta
import pytest

from domain.animals import Animal, Image
from repositories.inmemory.inmemory_animal_repo import InMemoryAnimalRepo

@pytest.fixture(scope='function')
def animals_list() -> list[dict]:
    return [
        {
            'name': 'Daisy',
            'color': 'white',
            'weight': 17,
            'birth_date': datetime(2020, 10, 1),
            'in_shelter_at': datetime(2021, 10, 1),
            'description': 'Funny dog',
            'id': 1,
            'images': [
                {'id': 1, 'relative_path': 'imgs/1.png', 'description': 'Some desc 1'},
                {'id': 3, 'relative_path': 'imgs/3.png', 'description': 'Some desc 3'},
            ],
        },
        {
            'name': 'Buffy',
            'color': 'white',
            'weight': 30,
            'birth_date': datetime(2021, 10, 1),
            'in_shelter_at': datetime(2022, 10, 1),
            'description': 'Super funny dog',
            'id': 2,
            'images': [
                {'id': 2, 'relative_path': 'imgs/2.png', 'description': 'Some desc 2'},
            ],
        },
    ]

class TestCreateAnimal:
    def test_inmemory_create_animal(self, animals_list: list[dict]):
        repo = InMemoryAnimalRepo(
            db_list=animals_list,
            base_images_path='imgs/')
        repo_start_len: int = len(repo)

        animal: Animal = Animal(
            name='Pufik',
            color='black',
            weight=7,
            birth_date=datetime(2019, 1, 1),
            in_shelter_at=datetime(2024, 1, 1),
            description='Pretty dog',
            images=[Image(name='funny.png', description='Super photo')],
        )
        saved_animal: Animal = repo.create(animal=animal)

        assert len(repo) == repo_start_len + 1
        assert saved_animal.id == repo_start_len + 1
        assert saved_animal.name == animal.name
        assert saved_animal.weight == animal.weight
        assert saved_animal.in_shelter_at == animal.in_shelter_at
        assert saved_animal.description == animal.description
        assert saved_animal.birth_date == animal.birth_date
        assert saved_animal.images
        assert saved_animal.images[0].id == 4
        assert saved_animal.images[0].name == 'funny.png'
        assert saved_animal.images[0].description == 'Super photo'
        assert saved_animal.images[0].relative_path == 'imgs/4.png'

class TestGetAnimalById:
    def test_inmemory_get_animal_by_id(self, animals_list: list[dict]):
        repo = InMemoryAnimalRepo(
            db_list=animals_list,
            base_images_path='imgs/')
        search_id: int = 1
        search_animal: Animal = repo.get_by_id(id=search_id)

        assert search_animal
        assert search_animal.id == search_id

    def test_inmemory_get_animal_by_id_not_found(self, animals_list: list[dict]):
        repo = InMemoryAnimalRepo(
            db_list=animals_list,
            base_images_path='imgs/')
        search_id: int = 100
        search_animal: Animal = repo.get_by_id(id=search_id)

        assert search_animal is None
