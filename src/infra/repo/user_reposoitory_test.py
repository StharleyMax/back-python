from faker import Faker
from .user_repository import UserRepository
from src.infra.config import DBConectionHandler

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
