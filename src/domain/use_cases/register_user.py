from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import Users


class RegisterUser(ABC):
    """interface to ResgisterUser use case"""

    @abstractmethod
    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """case"""
        raise Exception("Should implement method: register")
