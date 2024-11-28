from datetime import datetime, timezone, timedelta

from unittest.mock import MagicMock
import pytest
from domain.animals import Animal, Image
from repositories.base.animals_base_repository import BaseSyncAnimalRepository
from use_cases.animal_get_by_id_use_case import SyncAnimalGetByIdUseCase

def test_get_animal_by_id_success():
    mock_animal_repo = MagicMock(spec=BaseSyncAnimalRepository)

    use_case: SyncAnimalGetByIdUseCase = SyncAnimalGetByIdUseCase(
        animal_repo=mock_animal_repo,
    )

    animal_id: int = 3
    animal_obj: Animal = Animal(
        id=animal_id,
        name='Daysy',
        color='white',
        weight=17,
        birth_date=datetime(2020, 10, 1),
        in_shelter_at=datetime(2021, 10, 1),
        description='Funny dog',
        images=[
            Image(
                id=1,
                name='some_funny_image.png',
                relative_path='imgs/1.png',
                description='Funny',
            ),
        ],
    )
    mock_animal_repo.get_by_id.return_value = animal_obj

    res = use_case.execute(id=animal_id)
    assert res.id == animal_id
    assert res.name == 'Daysy'
    assert res.color == 'white'
    assert res.weight == 17
    assert res.birth_date == datetime(2020, 10, 1)
    assert res.in_shelter_at == datetime(2021, 10, 1)
    assert res.description == 'Funny dog'
    assert res.images[0].id == 1
    assert res.images[0].name == 'some_funny_image.png'
    assert res.images[0].relative_path == 'imgs/1.png'
    assert res.images[0].description == 'Funny'

    mock_animal_repo.get_by_id.assert_called_once_with(id=animal_id)

# def test_create_animal_not_admin():
#     mock_user_repo = MagicMock(spec=BaseSyncUserRepository)
#     mock_animal_repo = MagicMock(spec=BaseSyncAnimalRepository)

#     use_case: SyncAnimalCreateUseCase = SyncAnimalCreateUseCase(
#         user_repo=mock_user_repo,
#         animal_repo=mock_animal_repo,
#     )

#     not_admin_user: User = User(
#         name='Regular User',
#         email='regular@gmail.com',
#         phone='+79129999999',
#         password='password_hashed',
#         is_admin=False,
#         id=1,
#     )
#     mock_user_repo.get_by_id.return_value = not_admin_user
#     with pytest.raises(PermissionError):
#         creating_datetime: datetime = datetime.now(tz=timezone.utc)
#         animal_dict: dict = {
#             'name': 'Daisy',
#             'color': 'white',
#             'weight': 17,
#             'birth_date': datetime(2020, 10, 1),
#             'in_shelter_at': datetime(2021, 10, 1),
#             'created_at': creating_datetime,
#             'updated_at': creating_datetime + timedelta(1),
#             'description': 'Funny dog',
#         }
#         use_case.execute(
#             user_id=1,
#             name=animal_dict.get('name'),
#             color=animal_dict.get('color'),
#             weight=animal_dict.get('weight'),
#             birth_date=animal_dict.get('birth_date'),
#             in_shelter_at=animal_dict.get('in_shelter_at'),
#             created_at=animal_dict.get('created_at'),
#             updated_at=animal_dict.get('updated_at'),
#             description=animal_dict.get('description'),
#         )

#     mock_user_repo.get_by_id.assert_called_once_with(id=1)
#     mock_animal_repo.create.assert_not_called()
