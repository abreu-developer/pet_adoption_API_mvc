from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.controllers.pet_lister_controller import PetsListerController
from src.views.pet_lister_view import  PetListerView

def person_lister_composer():
    model = PetsRepository(db_connection_handler)
    controller = PetsListerController(model)
    view = PetListerView(controller)

    return view