from datetime import datetime, timezone, timedelta

from unittest.mock import MagicMock
import pytest
from domain.animals import Animal
from domain.users import User
from repositories.base.animals_base_repository import BaseSyncAnimalRepository
from repositories.base.users_base_repository import BaseSyncUserRepository
from use_cases.animal_create_use_case import SyncAnimalCreateUseCase

def test_create_animal_success():
    mock_user_repo = MagicMock(spec=BaseSyncUserRepository)
    mock_animal_repo = MagicMock(spec=BaseSyncAnimalRepository)

    use_case: SyncAnimalCreateUseCase = SyncAnimalCreateUseCase(
        user_repo=mock_user_repo,
        animal_repo=mock_animal_repo,
    )

    admin_user: User = User(
        name='Admin',
        email='admin@gmail.com',
        phone='+79129999999',
        password='password_hashed',
        is_admin=True,
        id=1,
    )
    mock_user_repo.get_by_id.return_value = admin_user

    creating_datetime: datetime = datetime.now(tz=timezone.utc)
    animal_dict: dict = {
        'name': 'Daisy',
        'color': 'white',
        'weight': 17,
        'birth_date': datetime(2020, 10, 1),
        'in_shelter_at': datetime(2021, 10, 1),
        'created_at': creating_datetime,
        'updated_at': creating_datetime + timedelta(1),
        'description': 'Funny dog',
    }
    new_animal: Animal = Animal(**animal_dict)

    animal_dict['id'] = 1
    saved_animal: Animal = Animal(**animal_dict)
    mock_animal_repo.create.return_value = saved_animal

    res = use_case.execute(
        user_id=1,
        name=animal_dict.get('name'),
        color=animal_dict.get('color'),
        weight=animal_dict.get('weight'),
        birth_date=animal_dict.get('birth_date'),
        in_shelter_at=animal_dict.get('in_shelter_at'),
        created_at=animal_dict.get('created_at'),
        updated_at=animal_dict.get('updated_at'),
        description=animal_dict.get('description'),
        )
    assert res.id == 1
    assert res.name == animal_dict.get('name')
    assert res.color == animal_dict.get('color')
    assert res.weight == animal_dict.get('weight')
    assert res.birth_date == animal_dict.get('birth_date')
    assert res.in_shelter_at == animal_dict.get('in_shelter_at')
    assert res.updated_at == animal_dict.get('updated_at')
    assert res.description == animal_dict.get('description')
    assert res.breed == 'breedless'
    assert res.coat == 'medium'
    assert res.type == 'dog'
    assert res.gender == 'male'
    assert res.status == 'available_for_adoption'
    assert res.ok_with_children == True
    assert res.ok_with_cats == True
    assert res.ok_with_dogs == True
    assert res.has_vaccinations == True
    assert res.is_sterilized == True

    mock_user_repo.get_by_id.assert_called_once_with(id=1)
    mock_animal_repo.create.assert_called_once_with(animal=new_animal)

def test_create_animal_not_admin():
    mock_user_repo = MagicMock(spec=BaseSyncUserRepository)
    mock_animal_repo = MagicMock(spec=BaseSyncAnimalRepository)

    use_case: SyncAnimalCreateUseCase = SyncAnimalCreateUseCase(
        user_repo=mock_user_repo,
        animal_repo=mock_animal_repo,
    )

    not_admin_user: User = User(
        name='Regular User',
        email='regular@gmail.com',
        phone='+79129999999',
        password='password_hashed',
        is_admin=False,
        id=1,
    )
    mock_user_repo.get_by_id.return_value = not_admin_user
    with pytest.raises(PermissionError):
        creating_datetime: datetime = datetime.now(tz=timezone.utc)
        animal_dict: dict = {
            'name': 'Daisy',
            'color': 'white',
            'weight': 17,
            'birth_date': datetime(2020, 10, 1),
            'in_shelter_at': datetime(2021, 10, 1),
            'created_at': creating_datetime,
            'updated_at': creating_datetime + timedelta(1),
            'description': 'Funny dog',
        }
        use_case.execute(
            user_id=1,
            name=animal_dict.get('name'),
            color=animal_dict.get('color'),
            weight=animal_dict.get('weight'),
            birth_date=animal_dict.get('birth_date'),
            in_shelter_at=animal_dict.get('in_shelter_at'),
            created_at=animal_dict.get('created_at'),
            updated_at=animal_dict.get('updated_at'),
            description=animal_dict.get('description'),
        )

    mock_user_repo.get_by_id.assert_called_once_with(id=1)
    mock_animal_repo.create.assert_not_called()
