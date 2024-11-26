from datetime import datetime
import pytest

from domain.users import User
from repositories.inmemory.inmemory_user_repo import InMemoryUserRepo

@pytest.fixture(scope='function')
def users_list() -> list[dict]:
    return [
        {
            'id': 1,
            'name': 'User1',
            'email': 'user1@gmail.com',
            'phone': '+79129999901',
            'password': 'password1_hashed',
        },
        {
            'id': 2,
            'name': 'User2',
            'email': 'user2@gmail.com',
            'phone': '+79129999902',
            'password': 'password2_hashed',
        },
        {
            'id': 3,
            'name': 'User3',
            'email': 'user3@gmail.com',
            'phone': '+79129999903',
            'password': 'password3_hashed',
        },
    ]


class TestCreateUser:
    def test_inmemory_create_user(self, users_list: list[dict]):
        repo = InMemoryUserRepo(db_list=users_list)
        repo_start_len: int = len(repo)

        user: User = User(
            name='User4',
            email='user4@gmail.com',
            phone='+79129999904',
            password='password4_hashed',
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


class TestGetUserByEmail:
    def test_inmemory_get_user_by_email(self, users_list: list[dict]):
        repo = InMemoryUserRepo(db_list=users_list)

        search_email: str = 'user3@gmail.com'
        search_user: User = repo.get_by_email(email=search_email)

        assert search_user
        assert search_user.email == search_email

    def test_inmemory_get_user_by_email_not_found(self, users_list: list[dict]):
        repo = InMemoryUserRepo(db_list=users_list)

        search_email: str = 'notfounded@gmail.com'
        search_user: User = repo.get_by_email(email=search_email)

        assert search_user is None


class TestGetAllUsers:
    def test_inmemory_get_all_users(self, users_list: list[dict]):
        repo = InMemoryUserRepo(db_list=users_list)

        all_users: list[User] = repo.get_all()

        assert all_users == [User.from_dict(user) for user in users_list]

    def test_inmemory_get_all_users_offset(self, users_list: list[dict]):
        repo = InMemoryUserRepo(db_list=users_list)

        offset: int = 1
        all_users: list[User] = repo.get_all(offset=offset)
        assert all_users == [User.from_dict(user) for index, user in enumerate(users_list) if index >= offset]

    def test_inmemory_get_all_users_offset_not_users(self, users_list: list[dict]):
        repo = InMemoryUserRepo(db_list=users_list)

        offset: int = 5
        all_users: list[User] = repo.get_all(offset=offset)
        assert all_users == []

    def test_inmemory_get_all_users_limit(self, users_list: list[dict]):
        repo = InMemoryUserRepo(db_list=users_list)

        limit: int = 2
        all_users: list[User] = repo.get_all(limit=limit)
        assert all_users == [User.from_dict(user) for index, user in enumerate(users_list)][:limit]

    def test_inmemory_get_all_users_limit_too_much(self, users_list: list[dict]):
        repo = InMemoryUserRepo(db_list=users_list)

        limit: int = 100
        all_users: list[User] = repo.get_all(limit=limit)
        assert all_users == [User.from_dict(user) for user in users_list]

    def test_inmemory_get_all_users_offset_limit(self, users_list: list[dict]):
        repo = InMemoryUserRepo(db_list=users_list)

        offset: int = 1
        limit: int = 1
        all_users: list[User] = repo.get_all(offset=offset, limit=limit)
        assert all_users == [User.from_dict(user) for index, user in enumerate(users_list) if index >= offset][:limit]


class TestDeleteUser:
    def test_inmemory_delete_user(self, users_list: list[dict]):
        repo = InMemoryUserRepo(db_list=users_list)
        repo_start_len: int = len(repo)

        user_id: int = 2
        repo.delete(id=user_id)
        assert len(repo) == repo_start_len - 1
        assert user_id not in [user.id for user in repo.get_all()]

    def test_inmemory_delete_user_(self, users_list: list[dict]):
        repo = InMemoryUserRepo(db_list=users_list)
        repo_start_len: int = len(repo)

        user_id: int = 2
        repo.delete(id=user_id)
        assert len(repo) == repo_start_len - 1
        assert user_id not in [user.id for user in repo.get_all()]

class TestGetUsersFiltered:
    pass
    #TODO