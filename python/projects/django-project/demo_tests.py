from dataclasses import dataclass
from typing import Literal


class GenericException(Exception):
    def __init__(self, message: str, code: int):
        super().__init__(message)
        self.message = message
        self.code = code

    def __str__(self):
        return f"{self.code}: {self.message}"


class NotMeowError(GenericException): ...


class NotOofError(GenericException): ...


@dataclass
class Animal:
    status: Literal["happy", "neutral", "sad"]

    def meow(self):
        raise NotMeowError(
            message=f"The {self.__class__.__name__} does not 'meow'!",
            code=1,
        )

    def oof(self):
        raise NotOofError(
            message=f"The {self.__class__.__name__} does not 'oof'!",
            code=2,
        )

    def pet(self):
        self.status = "happy"

    def check(self):
        return f"The {self.__class__.__name__} is {self.status}!"


@dataclass
class Cat(Animal):
    name: str

    def meow(self) -> str:
        return f"The cat {self.name} says 'meow'!"


@dataclass
class Dog(Animal):
    name: str

    def oof(self) -> str:
        return f"The dog {self.name} says 'oof'!"


if __name__ == "__main__":
    cat = Cat(name="Tom", status="neutral")
    cat.meow()
    cat.oof()
