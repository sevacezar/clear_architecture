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
        repo = InMemoryAnimalRepo(db_list=animals_list)
        repo_start_len: int = len(repo)

        animal: Animal = Animal(
            name='Pufik',
            color='black',
            weight=7,
            birth_date=datetime(2019, 1, 1),
            in_shelter_at=datetime(2024, 1, 1)
            description='Pretty dog',
            images=[Image(relative_path)]
        )
        saved_user: User = repo.create(user=user)

        assert len(repo) == repo_start_len + 1
        assert saved_user.id == repo_start_len + 1
        assert saved_user.name == 'User4'
        assert saved_user.email == 'user4@gmail.com'
        assert saved_user.phone == '+79129999904'
        assert saved_user.password == 'password4_hashed'
        assert saved_user.is_admin == False
        assert isinstance(saved_user.created_at, datetime)