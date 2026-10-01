from abc import ABC,abstractmethod

class PetsDeleteControllerInterface(ABC):

    @abstractmethod
    def delete_pets(self, name: str) -> None:
        pass