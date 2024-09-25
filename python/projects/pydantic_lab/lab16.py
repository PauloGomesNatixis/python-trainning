from typing import Callable, Dict, Union
from pydantic import BaseModel

# Define the Pydantic model for the 'all' function's return value
class OperationsModel(BaseModel):
    add: Callable[[Union[int, float]], Union[int, float]]
    subtract: Callable[[Union[int, float]], Union[int, float]]
    multiply: Callable[[Union[int, float]], Union[int, float]]
    divide: Callable[[Union[int, float]], Union[int, float]]
    power: Callable[[Union[int, float]], Union[int, float]]

class Calculator:
    def __init__(self, number: Union[int, float]):
        self.number: Union[int, float] = number

    def add(self, number: Union[int, float]) -> Union[int, float]:
        return self.number + number

    def subtract(self, number: Union[int, float]) -> Union[int, float]:
        return self.number - number

    def multiply(self, number: Union[int, float]) -> Union[int, float]:
        return self.number * number

    def divide(self, number: Union[int, float]) -> float:
        return self.number / number  # Division always returns float

    def power(self, number: Union[int, float]) -> Union[int, float]:
        return self.number ** number

    def all(self) -> OperationsModel:
        return OperationsModel(
            add=self.add,
            subtract=self.subtract,
            multiply=self.multiply,
            divide=self.divide,
            power=self.power
        )
