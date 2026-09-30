from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities.pets import PetsTable

from .pets_repository import PetsRepository


class MockConnectionError:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("no result found")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        pass


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetsTable)],
                    [
                        PetsTable(name="dog", type="dog"),
                        PetsTable(name="cat", type="cat"),
                    ],
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        pass


def test_list_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)

    response = repo.list_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)

    assert len(response) == 2
    assert response[0].name == "dog"
    assert response[1].name == "cat"


def test_list_pets_no_result():
    mock_connection = MockConnectionError()
    repo = PetsRepository(mock_connection)

    response = repo.list_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)

    assert response == []


def test_delete_pet():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)

    repo.delete_pets("pet_name")

    mock_connection.session.query.assert_called_once_with(PetsTable)


def test_delete_pet_error():
    mock_connection = MockConnection()
    mock_connection.session.delete.side_effect = Exception("error")

    repo = PetsRepository(mock_connection)

    with pytest.raises(Exception):
        repo.delete_pets("pet_name")

    mock_connection.session.rollback.assert_called_once()