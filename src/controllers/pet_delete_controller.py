from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface

from .interfaces.pet_delete_controller import PetsDeleteControllerInterface


class PetsDeleteController(PetsDeleteControllerInterface):
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def delete_pets(self, name: str) -> None:
        self.__pet_repository.delete_pets(name)