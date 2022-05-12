from faker import Faker
from src.infra.config import DBConectionHandler
from src.infra.entities import Users as UsersModel
from .user_repository import UserRepository


faker = Faker()
user_repository = UserRepository()
db_connection = DBConectionHandler()


def test_insert_user():
    """Should Insert User"""

    name = faker.name()
    password = faker.word()
    engine = db_connection.get_engine()

    new_user = user_repository.insert_user(name, password)
    query_user = engine.execute(
        "select * from users where id = '{}';".format(new_user.id)
    ).fetchone()
    engine.execute("delete from users where id = '{}';".format(new_user.id))
    print(new_user)
    print(query_user)

    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password


def test_select_user():
    """should select a user in users table and compare it"""

    user_id = faker.random_number(digits=5)
    name = faker.name()
    password = faker.word()
    data = UsersModel(id=user_id, name=name, password=password)

    engine = db_connection.get_engine()
    engine.execute(
        "insert into users(id, name, password) values ('{}','{}','{}')".format(
            user_id, name, password
        )
    )

    query_user1 = user_repository.select_user(user_id=user_id)
    query_user2 = user_repository.select_user(name=name)
    query_user3 = user_repository.select_user(user_id=user_id, name=name)

    assert data in query_user1
    assert data in query_user2
    assert data in query_user3

    engine.execute("delete from users where id = '{}'".format(user_id))
