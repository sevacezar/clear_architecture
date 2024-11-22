from datetime import datetime, timezone
import pytest

from domain.users import User

@pytest.fixture(scope='function')
def user_domain() -> User:
    user_dict: dict = {
        'id': 1,
        'name': 'John',
        'email': 'jphn@gmail.com',
        'phone': '+79129991212',
        'password': 'hashed_password',
        'is_admin': False,
        'created_at': datetime.now(tz=timezone.utc)
    }
    user: User = User(**user_dict)
    return user

def test_user_init():
    user_dict: dict = {
        'id': 1,
        'name': 'John',
        'email': 'jphn@gmail.com',
        'phone': '+79129991212',
        'password': 'hashed_password',
        'is_admin': False,
        'created_at': datetime.now(tz=timezone.utc)
    }
    user: User = User(**user_dict)
    assert user.id == user_dict.get('id')
    assert user.name == user_dict.get('name')
    assert user.email == user_dict.get('email')
    assert user.phone == user_dict.get('phone')
    assert user.password == user_dict.get('password')
    assert user.is_admin == user_dict.get('is_admin')
    assert user.created_at == user_dict.get('created_at')

def test_user_init_with_obligatory_attrs():
    user_dict: dict = {
        'name': 'John',
        'email': 'jphn@gmail.com',
        'phone': '+79129991212',
        'password': 'hashed_password',
    }
    user: User = User(**user_dict)
    assert user.id is None
    assert user.name == user_dict.get('name')
    assert user.email == user_dict.get('email')
    assert user.phone == user_dict.get('phone')
    assert user.password == user_dict.get('password')
    assert user.is_admin == False
    assert isinstance(user.created_at, datetime)

def test_user_from_dict():
    user_dict: dict = {
        'id': 1,
        'name': 'John',
        'email': 'jphn@gmail.com',
        'phone': '+79129991212',
        'password': 'hashed_password',
        'is_admin': False,
        'created_at': datetime.now(tz=timezone.utc)
    }
    user: User = User.from_dict(user_dict)
    assert user.id == user_dict.get('id')
    assert user.name == user_dict.get('name')
    assert user.email == user_dict.get('email')
    assert user.phone == user_dict.get('phone')
    assert user.password == user_dict.get('password')
    assert user.is_admin == user_dict.get('is_admin')
    assert user.created_at == user_dict.get('created_at')

def test_user_to_dict(user_domain: User):
    user_dict: dict = user_domain.to_dict()
    assert isinstance(user_dict, dict)
    assert user_domain.id == user_dict.get('id')
    assert user_domain.name == user_dict.get('name')
    assert user_domain.email == user_dict.get('email')
    assert user_domain.phone == user_dict.get('phone')
    assert user_domain.password == user_dict.get('password')
    assert user_domain.is_admin == user_dict.get('is_admin')
    assert user_domain.created_at == user_dict.get('created_at')

def test_user_update(user_domain: User):
    updated_params: dict = {
        'id': 3,
        'name': 'New name',
        'email': 'new_email@mail.ru',
        'phone': '+99999999999',
        'password': 'new_hashed_password',
        'is_admin': True,
    }
    updated_user: User = user_domain.update(updated_params)
    assert updated_user.id == updated_params.get('id')
    assert updated_user.name == updated_params.get('name')
    assert updated_user.email == updated_params.get('email')
    assert updated_user.phone == updated_params.get('phone')
    assert updated_user.password == updated_params.get('password')
    assert updated_user.is_admin == updated_params.get('is_admin')
