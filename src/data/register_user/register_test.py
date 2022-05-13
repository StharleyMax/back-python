from faker import Faker
from src.infra.test import UserRepositorySpy
from .register import RegisterUser

faker = Faker()


def test_register():
    """test registry method"""
    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)
    attr = {"name": faker.name(), "password": faker.name()}
    response = register_user.register(attr["name"], attr["password"])

    # Teste input
    assert user_repo.insert_user_param["name"] == attr["name"]
    assert user_repo.insert_user_param["password"] == attr["password"]

    # test Outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """test registry method"""
    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)
    attr = {"name": faker.random_number(), "password": faker.name()}

    response = register_user.register(attr["name"], attr["password"])

    # Teste input
    assert not user_repo.insert_user_param

    # test Outputs
    assert response["Success"] is False
    assert response["Data"] is None
