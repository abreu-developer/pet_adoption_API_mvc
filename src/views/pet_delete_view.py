from src.controllers.interfaces.pet_delete_controller import PetsDeleteControllerInterface
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse


class PetDeleteView(ViewInterface):
    def __init__(self, controller: PetsDeleteControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        name = http_request.param["name"]
        self.__controller.delete_pets(name)

        return HttpResponse(status_code=204)