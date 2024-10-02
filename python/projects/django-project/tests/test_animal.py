import pytest

from demo_tests import Animal, Cat, Dog


@pytest.fixture
def mock_animal():
    animal = Animal(status="neutral")
    print("Before test!")

    # Acima do yield roda ANTES do meu teste
    yield animal
    # Abaixo do yield roda DEPOIS do meu teste

    print("After test!")


@pytest.mark.parametrize(
    argnames="object_type, expected_value",
    argvalues=[
        (Cat, "The Cat is happy!"),
        (Dog, "The Dog is happy!"),
    ],
)
def test_animal(object_type, expected_value: str):
    animal_object = object_type(name="test", status="neutral")

    animal_object.pet()
    assert animal_object.check() == expected_value


def test_monkeypatch(monkeypatch):
    monkeypatch.setattr(Animal, "check", lambda _: "Overwrite return")

    animal = Animal(status="neutral")


def test_yield(mock_animal):
    print("Running test_yield!")


if __name__ == "__main__":
    pytest.main()
