from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetsListerController


class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(id=1, name="Buddy", type="Dog"),
            PetsTable(id=2, name="Mittens", type="Cat"),
            PetsTable(id=3, name="Charlie", type="Dog")
        ]


def test_list_pets():
    controller = PetsListerController(MockPetsRepository())
    response = controller.list_pets()

    expected_response = {
        "data": {
            "type": "pets",
            "count": 3,
            "attributes": [
                {
                    "name": "Buddy",
                    "type": "Dog",
                    "id": 1
                },
                {
                    "name": "Mittens",
                    "type": "Cat",
                    "id": 2
                },
                {
                    "name": "Charlie",
                    "type": "Dog",
                    "id": 3
                }
            ]
        }
    }

    assert response == expected_response