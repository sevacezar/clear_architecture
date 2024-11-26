from unittest.mock import MagicMock
import pytest

from domain.users import User
from domain.exceptions import UserAlreadyExists
from use_cases.user_create_use_case import SyncUserCreateUseCase


def test_create_user_success():
    user_dict: dict = {
        'name': 'John',
        'email': 'jphn@gmail.com',
        'phone': '+79129991212',
        'password': 'password',
    }
    mock_repo = MagicMock()
    mock_repo.get_by_email.return_value = None
    mock_repo.create.return_value = User(
        name=user_dict.get('name'),
        email=user_dict.get('email'),
        phone=user_dict.get('phone'),
        password=user_dict.get('password') + '_hashed',
    )

    use_case = SyncUserCreateUseCase(user_repo=mock_repo, hash_function=lambda x: x + '_hashed')
    user: User = use_case.execute(
        name=user_dict.get('name'),
        email=user_dict.get('email'),
        phone=user_dict.get('phone'),
        password=user_dict.get('password'),
    )

    # Checking function calls with correct arguments
    mock_repo.get_by_email.assert_called_once_with(email=user_dict.get('email'))
    mock_repo.create.assert_called_once_with(user=User(
        name=user_dict.get('name'),
        email=user_dict.get('email'),
        phone=user_dict.get('phone'),
        password=user_dict.get('password') + '_hashed',
    ))

    assert user.id is None
    assert user.name == user_dict.get('name')
    assert user.email == user_dict.get('email')
    assert user.phone == user_dict.get('phone')
    assert user.password == user_dict.get('password') + '_hashed'
    assert user.is_admin == False

def test_create_user_already_exists():
    user_dict: dict = {
        'name': 'John',
        'email': 'jphn@gmail.com',
        'phone': '+79129991212',
        'password': 'password',
    }
    mock_repo = MagicMock()
    mock_repo.get_by_email.return_value = User(
        name=user_dict.get('name'),
        email=user_dict.get('email'),
        phone=user_dict.get('phone'),
        password=user_dict.get('password') + '_hashed',
    )
    use_case = SyncUserCreateUseCase(user_repo=mock_repo, hash_function=lambda x: x + '_hashed')
    with pytest.raises(UserAlreadyExists):
        user: User = use_case.execute(
            name=user_dict.get('name'),
            email=user_dict.get('email'),
            phone=user_dict.get('phone'),
            password=user_dict.get('password'),
        )
