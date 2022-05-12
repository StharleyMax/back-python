from faker import Faker
from src.infra.config import DBConectionHandler
from .pet_repository import PetRepository


faker = Faker()
pet_repository = PetRepository()
db_connection = DBConectionHandler()


def test_insert_pet():
    """Should insert pet in Pet table"""

    name = faker.name()
    specie = "DOG"
    age = faker.random_number(digits=1)
    user_id = faker.random_number()

    # SQL Commands
    new_pet = pet_repository.insert_pet(name, specie, age, user_id)
    engine = db_connection.get_engine()
    query_pet = engine.execute(
        "SELECT * FROM pets WHERE id = '{}';".format(new_pet.id)
    ).fetchone()

    assert new_pet.id == query_pet.id
    assert new_pet.age == query_pet.age
    assert new_pet.specie == query_pet.specie
    assert new_pet.name == query_pet.name
    assert new_pet.user_id == query_pet.user_id

    engine.execute("delete from pets where id = '{}'".format(new_pet.id))
