from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Pets


class PetRepositoryInterface(ABC):
    """interface to Pet Repository"""

    @abstractmethod
    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> Pets:
        """abstractmethod"""
        raise Exception("Method not implement")

    @abstractmethod
    def select_pet(self, pet_id=None, user_id=None) -> List[Pets]:
        """abstractmethod"""
        raise Exception("Method not implement")
