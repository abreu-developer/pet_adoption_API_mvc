from src.controllers.pet_delete_controller import PetsDeleteController

def test_delete_pet(mocker):
    mock_repository = mocker.Mock()
    controller = PetsDeleteController(mock_repository)
    controller.delete_pets("amiginho")

    mock_repository.delete_pets.assert_called_once_with("amiginho")