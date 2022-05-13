from typing import List
from src.domain.models import Users
from src.domain.test import mock_users


class UserRepositorySpy:
    """spy to user repository"""

    def __init__(self):
        self.insert_user_param = {}
        self.select_user_param = {}

    def insert_user(self, name: str, password: str) -> Users:
        """Spy to all attributes"""
        self.insert_user_param["name"] = name
        self.insert_user_param["password"] = password

        return mock_users()

    def select_user(self, user_id: int = None, name: str = None) -> List[Users]:
        """Spy to all Attributes"""
        self.insert_user_param["name"] = name
        self.insert_user_param["user_id"] = user_id
