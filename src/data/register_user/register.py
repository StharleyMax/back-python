from typing import Dict, Type
from src.domain.models.users import Users
from src.domain.use_cases import RegisterUser as RegisterUserInterface
from src.data.interfaces import UserRepositoryInterface as UserRepository


class RegisterUser(RegisterUserInterface):
    """class to define use case: Register User"""

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """
        Register use case
        :param: - name: person name
                - password: password of the person
        :return - Dictionary with information  of the process
        """

        response = None
        validate_entry = isinstance(name, str) and isinstance(password, str)

        if validate_entry:
            response = self.user_repository.insert_user(name, password)

        return {"Success": validate_entry, "Data": response}
