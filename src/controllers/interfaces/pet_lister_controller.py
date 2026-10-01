from abc import ABC,abstractmethod

class PetsListerControllerInterface(ABC):

    @abstractmethod
    def list_pets(self) -> dict:
        pass