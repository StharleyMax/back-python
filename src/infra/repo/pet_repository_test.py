from faker import Faker
from src.infra.config import DBConectionHandler
from src.infra.entities import Pets
from src.infra.entities.pets import AnimalTypes
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


def test_select_pet():
    """Should select a pet in Pets table and compare ir"""

    pet_id = faker.random_number(digits=4)
    name = faker.name()
    specie = "DOG"
    age = faker.random_number(digits=1)
    user_id = faker.random_number()

    specie_mock = AnimalTypes("DOG")
    data = Pets(id=pet_id, name=name, specie=specie_mock, age=age, user_id=user_id)

    # SQL Commands
    engine = db_connection.get_engine()
    engine.execute(
        "insert into pets (id, name, specie, age, user_id) values ('{}','{}','{}','{}','{}')".format(
            pet_id, name, specie, age, user_id
        )
    )

    query_pets1 = pet_repository.select_pet(pet_id=pet_id)
    query_pets2 = pet_repository.select_pet(pet_id=pet_id, user_id=user_id)
    query_pets3 = pet_repository.select_pet(user_id=user_id)

    assert data in query_pets1
    assert data in query_pets2
    assert data in query_pets3

    engine.execute("delete from pets where id = '{}'".format(data.id))
